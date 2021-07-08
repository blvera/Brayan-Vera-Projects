# Project 1 Report

### 1. General Structure

We adopt a data struct to store command. The struct command_line contains two 
variables. The first one stores the name of the command. The second one stores 
the list of arguments as a list of strings. This include the command name, so 
it can be passed to exec() directly.
The main() function of our sshell is an infinite while loop. Inside the loop, 
we have 5 steps to take:

* Print prompt and read user input. This part adapts from sshell_tester.c 
provided by the professor.
* Parse input the check if the input is valid: inputs are parsed manually 
in order to deal with special characters ('<', '>', '|' and '&'). Details 
on handling them will be discussed in other sectionss. In general, our 
function read character by character, and store the value inside a 
temporary string. When there is a space, it marks it. The copying from the
temporary string to the actual structure array only happens when next 
non-space character is reached. Therefore, it can handle the condition that 
the arguments are seperated by more than one whitespaces.
* execute the command: Two builtin commands need to be executed at the 
parent level. "exit" will always be checked first and then "cd". For 
other external commands and "pwd", we applied fork + exec + wait method. 
Commands were run by the child inside a function. 
* wait for the child to terminate and print information message: Sshell is 
the parent.
* free allocated memory


Many functions we used would return -1 if an error occur. Checks for different
errors happen at different phases of parsing, so we can have them seperated.

### 2. Redirection
##### functions involved:
* Check_Red_File_Valid
* Input_Redirect
* Output_Redirect

We added 2 new variables in struct to store the input file name and output 
file name. They contain the names only if a redirection arrow appears, 
otherwise, they will be NULL. In the parsing, we first check the presence of 
redirection arrows. They are generally treated like whitespaces, besides we 
rise a special flag to indicate that the upcoming parsed word should be stored 
into the corresponding file name varialbes, not in arguments. When we are 
executing the command, we will check if the file names are NULL. If a name is 
not NULL, we will call the corresponding function to perform redirection. It 
is adapted from the skeleton code on the lecture slides. We open the file, and 
connect it with stdin or stdout using dup2().

### 3. Pipeline
##### functions involved:
* Check_Pipeline
* Parse_Pipe
* Execution_Pipe
* Pipe_Connection

In order to deal with pipeline command, in each loop, we consruct an array of 
our struct command_line. This array will be allocated dynamically based on the 
number of commands there are inside the pipe. With the parsing, we first use a 
function to chop this input string into substrings. And then parse each 
substring and store information into corresponding structs. In execution, the 
sshell will fork and creat a child. That child will continue to fork and 
create children such that each child runs one command in pipeline. Therefore, 
it is the grandchildren of sshell running the commands. The child fork and 
pipe in a loop manner. In the loop, it will create a pipe, fork, and the 
grandchildren will connect its stdin and stdout to pipes. The first grandchild 
and the last grandchildren are treated differently, for they will still read 
partially from stdin and stdout. The child will wait for all grandchildren to 
terminate and collect exit status. It will process exit status into a string 
and pass that string to sshell by a pipe. So the execution of all commands in the pipeline are bundled together.

### 4. Background

We haven't got time to implement this part, but we want to talk about the 
design. In order to keep track of all commands being running, the sshell 
should have a list of running processes. Therefore, we defined structure 
process. It contains the pid of the child running the command, a string of 
original input so you can print the right prompt, a bool indicating if its a 
pipeline command, the id of the pipe between sshell and the child running 
pipeline command, and a bool indicating if it should run in background. After 
parsing the string and fork a child to run, we store correponding information 
inside the struct. The list will be ordered by the time the command was 
called. Then at step 4, you check every running process in the list. If its a 
background command, don't wait until it terminates (can use flag WNOHANG in 
waitpid()). Otherwise, wait for it. And then print out the right information 
message. We will remove the terminated process from the list. Another function 
should be triggered is that, when the user press only enter (input string is 
'\n'), don't execute but check the list of running processes. Print 
information message if any of them terminated. Another flag active_job will be 
true when the list is not empty. We will do another check when the user tries 
to exit. If active_job is true, print error message and don't exit for there 
are still processes running in the background.

#### reference
1. <https://stackoverflow.com/questions/298510/
how-to-get-the-current-directory-in-a-c-program>
2. <https://stackoverflow.com/questions/8082932/
connecting-n-commands-with-pipes-in-a-shell>
We also want to give special thanks to tutor Sean Young for explaining 
redirection and TA John Chan for confirming our idea on background command 
although we don't have time to code.
