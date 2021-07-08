#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>

#define CMDLINE_MAX 512

//error code
enum {
	ERR_INV_CMD,
	ERR_CMD_NOT_FOUND,
	ERR_NO_DIR,
	ERR_MIS_BACK_SIGN,
	ERR_ACT_JOB,
	ERR_OPEN_IN_FILE,
	ERR_NO_IN_FILE,
	ERR_OPEN_OUT_FILE,
	ERR_NO_OUT_FILE,
	ERR_MISLOC_IN_RE,
	ERR_MISLOC_OUT_RE,
};

struct command_line {
	char *file;
	char *arg[17];
	char *file_in;
	char *file_out;
};

struct process {
	pid_t pid;
	char buffer[512];
	bool pipe;
	int pipefd[2];
	bool background;
};


/*--------------------------------------------function declaration-----------------------------------------------------*/
/*valid input check functions:*/
int Check_Spec_Char(char *buffer);
int Check_Pipeline(char *buffer);
int Check_Red_File_Valid (struct command_line *cmd, int num_cmd);
//print correponding error message based on the error code
void Err_Msg(int err_code);

/*parsing functions*/
//parse a string based on '|'
void Parse_Pipe(char *buffer, char **pipe_parsed);
//parse a string based on whitespace
int Parsing(struct command_line *ptr_cmd, char *buffer, bool *background);
//copy string in temp into the right position in cmd
void Move_Temp(char temp[CMDLINE_MAX], struct command_line *ptr_cmd, int num_args);

/*execution fuctions:*/
bool Builtin_Cmd(struct command_line cmd, int *status);
pid_t Execution(struct command_line *cmd, char *buffer, int num_cmd, char **exit_status, int *pipefd);
void Execution_Pipe(struct command_line *cmd, char *buffer, int num_cmd, pid_t **ptr_pid);
pid_t Pipe_Connection (int in, int out, struct command_line *cmd);

/*free memory functions:*/
void Free_Cmd(int num_args, struct command_line *cmd);

/*general purpose functions:*/
//convert an integer array into a string with format "[num_1][num_2]...[num_n]"
void Int_To_String(int *array, int arr_len, char **string);

/*redirection functions:*/
void Input_Redirect (struct command_line cmd);
void Output_Redirect (struct command_line cmd);



/*--------------------------------------------main()-----------------------------------------------------*/
int main(int argc, char *argv[]) {
	char buffer[CMDLINE_MAX];
	bool active_job = false;


	while (1) {
		char *nl;



		/*1. print prompt and read input from user*/

		printf("sshell$ ");
		fflush(stdout);
		fgets(buffer, CMDLINE_MAX, stdin);

		//echoes command line to stdout if fgets read from a file and not the terminal
		if(!isatty(STDIN_FILENO)) {
			printf("%s", buffer);
			fflush(stdout);
		}
		//remove the trailing '\n'
		nl = strchr(buffer, '\n');
		if (nl)
			*nl = '\0';



		/*2. parse input and check if input is valid*/

		//Check if input is a special character
		if (Check_Spec_Char(buffer) == ERR_INV_CMD) {
			Err_Msg(ERR_INV_CMD);
			continue;
		}

		bool background = false;
		struct command_line *cmd;
		//check how many commands are inside the pipeline
		int num_cmd = Check_Pipeline(buffer);

		if (num_cmd == -1) {
			Err_Msg(ERR_MIS_BACK_SIGN);
			continue;
		}
		cmd = (struct command_line *)malloc(num_cmd * sizeof(struct command_line));

		//parse input based on '|', store resulting substrings as a list of strings
		char **pipe_parsed = (char **)malloc(num_cmd * sizeof(char *));
		Parse_Pipe(buffer, pipe_parsed);

		//parse input
		int num_args[num_cmd];
		int code;
		for(int i = 0; i < num_cmd; i++) {
			cmd[i].file_in = NULL;
			cmd[i].file_out = NULL;
			code = Parsing(cmd+i, pipe_parsed[i], &background);

			//not the first command in the pipeline but have input redirected
			if ((i != 0) && (cmd[i].file_in != NULL)) {
				Err_Msg(ERR_MISLOC_IN_RE);
				code = -1;
			}

			//not the last command in the pipeline but have output redirected
			if ((i != num_cmd - 1) && (cmd[i].file_out != NULL)) {
				Err_Msg(ERR_MISLOC_OUT_RE);
				code = -1;
			}

			//error in redirection
			if (code == -1) {
				break;
			} 
			//no error, return value is number of arguments in current command
			else {
				num_args[i] = code;
			}
		}
		if (code == -1) {
			continue;
		}

		//check if there is error in opening input or output file
		if (Check_Red_File_Valid (cmd, num_cmd) == -1) {
			continue;
		}



		/*3. execute the command*/

		//builtin command: exit
		if (strcmp(cmd[0].file, "exit") == 0) {
			if (active_job) {
				Err_Msg(ERR_ACT_JOB);
			} else {
				fprintf(stderr, "Bye...\n");
				return EXIT_SUCCESS;
			}
		}
		//builtin command: cd
		else if (strcmp(cmd[0].file, "cd") == 0) {
			int stat = chdir(cmd[0].arg[1]);

			if (stat == -1) {
				Err_Msg(ERR_NO_DIR);
			}
			fprintf(stderr, "+ completed '%s' [%d]\n", buffer, abs(stat));

			continue;
		}


		char *exit_status = (char *)malloc(CMDLINE_MAX * sizeof(char));
		int pipefd[2];

		pid_t pid = Execution(cmd, buffer, num_cmd, &exit_status, pipefd);


		/*4. wait for the child to terminate and print information message*/
		if (num_cmd > 1) {
			waitpid(pid, NULL, 0);

			//read the string of pipeline commands exit status from its child
			read(pipefd[0], exit_status, CMDLINE_MAX);
		} else {
			int status[num_cmd];
			int e_status[num_cmd];
			waitpid(pid, status, 0);

			e_status[0] = WEXITSTATUS(status[0]);
			Int_To_String(e_status, num_cmd, &exit_status);
		}

		//print output of program execution
		fprintf(stderr, "+ completed '%s' %s\n", buffer, exit_status);

		memset(exit_status, 0, strlen(exit_status));
		free(exit_status);
		exit_status = NULL;
		



		/*5. free allocated memory*/

		for(int i = 0; i < num_cmd; i++) {
			Free_Cmd(num_args[i], cmd+i);
		}
		free(cmd);
		cmd = NULL;

		for(int i = 0; i < num_cmd; i++) {
			free(pipe_parsed[i]);
			pipe_parsed[i] = NULL;
		}
		free(pipe_parsed);
		pipe_parsed = NULL;

	}


	return EXIT_SUCCESS;
}




/*--------------------------------------------function definition-----------------------------------------------------*/

/*valid input check functions:*/
int Check_Spec_Char(char *buffer) {
	if ((strcmp(buffer, "&") == 0)||(strcmp(buffer, "<") == 0)||(strcmp(buffer, ">") == 0)||(strcmp(buffer, "|") == 0)) {
		return ERR_INV_CMD;
	}

	return -1;
}

int Check_Pipeline(char *buffer) {
	int num_cmd = 0;

	//count the number of pipes
	for(int i = 0; i < strlen(buffer); i++) {
		if (buffer[i] == '|') {
			++num_cmd;
		}
		//background sign appear not as the last sign rises up an error
		else if ((buffer[i] == '&')&&(i != strlen(buffer)-1)) {
			return -1;
		}
	}

	return num_cmd + 1;
}

int Check_Red_File_Valid (struct command_line *cmd, int num_cmd) {
	int err;
	int fd;

	//if there is input redirection
	if (cmd[0].file_in != NULL) {
		fd = open(cmd[0].file_in, O_RDONLY);

		//if cannot open the file
		if (fd == -1) {
			Err_Msg(ERR_OPEN_IN_FILE);
			err = -1;
		} else {
			close(fd);
		}
	}


	//if there is output redirection
	if (cmd[num_cmd-1].file_out != NULL) {
		fd = open(cmd[num_cmd-1].file_out, O_RDWR|O_CREAT, 0644);

		//cannot open the file
		if (fd == -1) {
			Err_Msg(ERR_OPEN_OUT_FILE);
			err = -1;
		} else {
			close(fd);
		}
	}

	return err;
}

//print correponding error message based on the error code
void Err_Msg(int err_code) {
	switch (err_code) {
		case ERR_INV_CMD:
			fprintf(stderr, "Error: invalid command line\n");
			break;

		case ERR_CMD_NOT_FOUND:
			fprintf(stderr, "Error: command not found\n");
			break;

		case ERR_NO_DIR:
			fprintf(stderr, "Error: no such directory\n");
			break;

		case ERR_MIS_BACK_SIGN:
			fprintf(stderr, "Error: mislocated background sign\n");
			break;

		case ERR_ACT_JOB:
			fprintf(stderr, "Error: active jobs still running\n");
			break;

		case ERR_OPEN_IN_FILE:
			fprintf(stderr, "Error: cannot open input file\n");
			break;

		case ERR_NO_IN_FILE:
			fprintf(stderr, "Error: no input file\n");
			break;

		case ERR_OPEN_OUT_FILE:
			fprintf(stderr, "Error: cannot open output file\n");
			break;

		case ERR_NO_OUT_FILE:
			fprintf(stderr, "Error: no output file\n");
			break;

		case ERR_MISLOC_IN_RE:
			fprintf(stderr, "Error: mislocated input redirection\n");
			break;

		case ERR_MISLOC_OUT_RE:
			fprintf(stderr, "Error: mislocated output redirection\n");
			break;
	}
}


/*parsing functions*/
//parse a string based on '|'
void Parse_Pipe(char *buffer, char **pipe_parsed) {
	char temp[CMDLINE_MAX];
	int cur_cmd = 0;
	int j = 0;

	for(int i = 0; i < strlen(buffer); i++) {
		if (buffer[i] == '|') {
			pipe_parsed[cur_cmd] = (char *)malloc(strlen(temp)+1);
			strcpy(pipe_parsed[cur_cmd], temp);

			cur_cmd++;
			//clean temp and reset location indcator
			j = 0;
			memset(temp, 0, strlen(temp));
		} else {
			temp[j] = buffer[i];
			temp[j+1] = '\0';
			j++;
		}
	}

	//to store last string after the last '|'
	pipe_parsed[cur_cmd] = (char *)malloc(strlen(temp));
	strcpy(pipe_parsed[cur_cmd], temp);
	memset(temp, 0, strlen(temp));
}

//parse a string based on whitespace
int Parsing(struct command_line *ptr_cmd, char *buffer, bool *background) {
	char temp[CMDLINE_MAX];
	int num_args = 0;
	int i, j = 0;
	bool was_space = false;		//the last char was a whitespace
	bool is_beginning = true;	//we are at the beginning of the string; or we just past a redirection arrow
	bool in = false;			//the last char was a '<'
	bool out = false;			//the last char was a '>'

	for(i = 0; i < strlen(buffer); i++){
		if (buffer[i] == ' ') {
			was_space = true;
		} else if (buffer[i] == '&') {
			*background = true;
		} else if (buffer[i] == '>') {
			out = true;

			Move_Temp(temp, ptr_cmd, num_args);
			++num_args;

			//empty temp and initiate j
			memset(temp, 0, strlen(temp));
			j = 0;

			was_space = true;
			is_beginning = true;
		} else if (buffer[i] == '<') {
			in = true;

			Move_Temp(temp, ptr_cmd, num_args);
			++num_args;

			//empty temp and initiate j
			memset(temp, 0, strlen(temp));
			j = 0;

			was_space = true;
			is_beginning = true;
		} else {
			//if last char is space, copy string from temp into the right arg[] and also file
			//but some strings start with space, so don't do it if it's the beginning of a string
			if (was_space && !is_beginning) {
				if (in) {			//input file name
					ptr_cmd->file_in = malloc(strlen(temp)+1);
					strcpy(ptr_cmd->file_in, temp);

					in = false;
				} else if (out) {	//output file name
					ptr_cmd->file_out = malloc(strlen(temp)+1);
					strcpy(ptr_cmd->file_out, temp);

					out = false;
				} else {			//arguement
					Move_Temp(temp, ptr_cmd, num_args);
					++num_args;
				}

				//empty temp and initiate j
				memset(temp, 0, strlen(temp));
				j = 0;

				was_space = false;
			}

			//upadte temp
			temp[j] = buffer[i];
			temp[j+1] = '\0';
			j++;

			is_beginning = false;
			was_space = false;
		}
	}

	if ((strlen(temp) == 0) && in) {
		Err_Msg(ERR_NO_IN_FILE);

		return -1;
	} else if ((strlen(temp) == 0) && out) {
		Err_Msg(ERR_NO_OUT_FILE);

		return -1;
	}


	//this is used to store the last arg which is not followed by any space
	if (in) {			//input file name
		ptr_cmd->file_in = malloc(strlen(temp)+1);
		strcpy(ptr_cmd->file_in, temp);

		in = false;
	} else if (out) {	//output file name
		ptr_cmd->file_out = malloc(strlen(temp)+1);
		strcpy(ptr_cmd->file_out, temp);

		out = false;
	} else {			//arguement
		temp[j] = '\0';
		Move_Temp(temp, ptr_cmd, num_args);
		++num_args;
	}

	//cleaning temp
	memset(temp, 0, strlen(temp));

	//set the last element in arg[] to be NULL
	ptr_cmd->arg[num_args] = NULL;

	return num_args;
}

//copy string in temp into the right position in cmd
void Move_Temp(char temp[CMDLINE_MAX], struct command_line *ptr_cmd, int num_args) {
	//the first argument is also the name of the command
	if (num_args == 0) {
		ptr_cmd->file = (char *)malloc(strlen(temp)+1);
		strcpy(ptr_cmd->file, temp);
	}

	ptr_cmd->arg[num_args] = malloc(strlen(temp)+1);
	strcpy(ptr_cmd->arg[num_args], temp);
}


/*execution fuctions:*/
bool Builtin_Cmd(struct command_line cmd, int *status) {	
	//builtin command: pwd
	if (strcmp(cmd.file, "pwd") == 0) {
		char cwd[CMDLINE_MAX];
		//https://stackoverflow.com/questions/298510/how-to-get-the-current-directory-in-a-c-program
		if (getcwd(cwd, CMDLINE_MAX) != NULL){
			fprintf(stdout,"%s\n", cwd);
			*status = 0;
			//fprintf(stderr, "+ completed '%s' [0]\n", buffer);
		} else {
			*status = 1;
			//fprintf(stderr, "+ completed '%s' [1]\n", buffer);
		}

		return true;
	}
	//builtin command: cd
	else if (strcmp(cmd.file, "cd") == 0) {
		int stat = chdir(cmd.arg[1]);

		if (stat == -1) {
			Err_Msg(ERR_NO_DIR);
			*status = 1;
		} else {
			*status = 0;
		}
		//fprintf(stderr, "+ completed '%s' [%d]\n", buffer, abs(stat));

		return true;
	}

	return false;
}

pid_t Execution(struct command_line *cmd, char *buffer, int num_cmd, char **exit_status, int *pipefd) {
	pid_t pid;

	//pipeline command
	if (num_cmd > 1) {
		//creat pipe to communicate between parent and child
		pipe(pipefd);

		pid = fork();
		if (pid == 0) {	//child
			close(pipefd[0]);

			int status[num_cmd];
			int e_status[num_cmd];
			pid_t *pid_child = (pid_t *)malloc(num_cmd * sizeof(pid_t));

			Execution_Pipe(cmd, buffer, num_cmd, &pid_child);

			//wait for all its children to terminate
			for(int i = 0; i < num_cmd; i++) {
				waitpid(pid_child[i], status+i, 0);
				e_status[i] = WEXITSTATUS(status[i]);
			}

			//write the string of pipeline commands exit status to sshell
			Int_To_String(e_status, num_cmd, exit_status);
			write(pipefd[1], *exit_status, CMDLINE_MAX);

			free(pid_child);
			pid_child = NULL;

			exit(0);
		} else if (pid > 0) {	//parent
			close(pipefd[1]);

			return pid;	
		} else {	//error
			perror("Error: fork()");
			exit(1);
		}
	} 
	//only one command
	else {
		pid = fork();

		if (pid == 0) { //child
			if (cmd[0].file_in != NULL) {
				Input_Redirect(*cmd);
			}

			if (cmd[0].file_out != NULL) {
				Output_Redirect(*cmd);
			}

			int sta;
			if (Builtin_Cmd(cmd[0], &sta)) {
				exit(sta);
			} else {
				execvp(cmd[0].file, cmd[0].arg);
				Err_Msg(ERR_CMD_NOT_FOUND);
				exit(1);
			}			
		} else if (pid > 0) {	//parent
			return pid;
		} else {
			perror("Error: fork()");
			exit(1);
		}
	}

	return pid;
}

//create pipe and fork based on the number of commands
void Execution_Pipe(struct command_line *cmd, char *buffer, int num_cmd, pid_t **ptr_pid) {
	int fd[2];
	int i = 0;
	int in = 0;

	//commands that are not the last command should connect stdout to pipe
	for(i = 0; i < num_cmd-1; i++) {
		pipe(fd);

		(*ptr_pid)[i] = Pipe_Connection(in, fd[1], cmd+i);

		close(fd[1]);
		in = fd[0];
	}

	//the last command in pipeline
	(*ptr_pid)[i] = fork();
	if((*ptr_pid)[i] == 0) {
		if (cmd[num_cmd-1].file_out != NULL) {
			Output_Redirect(cmd[num_cmd-1]);
		}

		dup2(in, STDIN_FILENO);
		close(in);
		close(fd[1]);

		int sta;
		if (Builtin_Cmd(cmd[num_cmd-1], &sta)) {
			exit(sta);
		} else {
			execvp(cmd[num_cmd-1].file, cmd[num_cmd-1].arg);
			Err_Msg(ERR_CMD_NOT_FOUND);
			exit(1);
		}
	}
}

pid_t Pipe_Connection (int in, int out, struct command_line *cmd) {
	pid_t pid = fork();

	if (pid == 0) {
		if (cmd->file_in != NULL) {
			Input_Redirect(*cmd);
		}

		//if there is a pipe it should connect to read info
		if (in != 0) {
			//connect stdin to pipe in front of it
			dup2(in, STDIN_FILENO);
			close(in);
		}

		//connect stdoout to pipe after it
		dup2(out, STDOUT_FILENO);
		close(out);

		int sta;
		if (Builtin_Cmd(*cmd, &sta)) {
			exit(sta);
		} else {
			execvp(cmd->file, cmd->arg);
			Err_Msg(ERR_CMD_NOT_FOUND);
			exit(1);
		}
	}

	return pid;
}


/*free memory functions:*/
void Free_Cmd(int num_args, struct command_line *cmd) {
	free(cmd->file);
	cmd->file = NULL;

	if (cmd->file_in != NULL) {
		free(cmd->file_in);
		cmd->file_in = NULL;
		
	}
	if (cmd->file_out != NULL) {
		free(cmd->file_out);
		cmd->file_out = NULL;
		
	}

	for(int i = 0; i < num_args; i++) {
		free(cmd->arg[i]);
		cmd->arg[i] = NULL;
	}
}


/*general purpose functions:*/
//convert an integer array into a string with format "[num_1][num_2]...[num_n]"
void Int_To_String(int *array, int arr_len, char **string) {
	char temp[6];
	int len = 0;

	for (int i = 0; i < arr_len; i++) {

		//store current integer into temp
		sprintf(temp, "[%d]", array[i]);

		//concatenate temp to string
		strcpy(*string+len, temp);
		len = len + strlen(temp);

		//clear temp
		memset(temp, 0 ,strlen(temp));
	}
}


/*redirection functions:*/
void Input_Redirect (struct command_line cmd) {
	int fd = open(cmd.file_in, O_RDONLY);

	dup2(fd, STDIN_FILENO);
	close(fd);
}

void Output_Redirect (struct command_line cmd) {
	int fd = open(cmd.file_out, O_WRONLY|O_CREAT, 0644);

	dup2(fd, STDOUT_FILENO);
	close(fd);
}
