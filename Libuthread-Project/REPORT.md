## REPORT

### Phase 1: Queue API
The queue was built function by function. I first read the function description
located in the header file then wrote the main body of each function to match
the description. When a majority of the function bodys were coded, I went back
and wrote in the required error handlers. The structure I went with for the
queue was akin to a linked list, because it allows for easy expansion and
dequeueing. This method also made the delete queue function simple, because
erasing an item in a linked list is very straight forward.

The makefile caused the most issues and confusion for phase 1. When
implementing the makefile within libuthread, I was faced with cryptic errors
that were not helping me with the debug process. Every method I implemented
both short hand ($^, $>, ..) and long hand were giving crypting errors. I
finally debugged and found the issue was the lack of main in the queue_test.
After this small fix, the makefile was cleaned up and written in short hand
notation to make adding the other C files easy down the road.

On top of the provided simple tests, I added test cases that covered many
different senerios. Tested things such as deleting from front, deleting from the
back, deleting from the middle, enquing multiple things in a row, and dequeueing
multiple things in a row, enquing NULL, and usage of the iterate function. The
advanced tests showed a few small bug with the deletion process and one larger
bug within the queue when using the iterate function. After a long debugging
process, it turned out that the issue was with the way I initially implemented
my custom queue print fucntion. Once that was resolved, the testing process
concluded and we were good to proceed to phase 2.
###### Resources used in phase 1:
* [Linked Lists] - Refresher on linked list data structures
* [GeeksForGeeks Delete Node] - Properly deleting nodes from a linked list

### Phase 2: Uthread API
Our primary task for this phase was understanding the demo code provided by
professor Porquet. In addition, understanding the API documentation was also
essential to build our knowledge with enough material before starting this
phase.

We accomplished this phase by following the instructions carefully from the
ucontext.h file and also the instructions document (section 5.3) for this
project.

We programmed this phase function by function. But, first, we defined our thread
data structure, global variables, and queue structures at the top of our code in
order to define our user thread. This was essential because since we are
creating multiple threads, we need to keep track of the TID (Thread Identifier),
state (whether our thread is in running, ready, blocked or zombie mode), the
“stack” of each thread, and the CPU registers of each thread (used to save the
thread when restoring it later).

We started with the uthread_create() function. For this function, our task was
to create a thread and generate new threads. To do this, this function first
calls a “static void thread_0()” helper function that we included in order to
have our main thread there where the state of ready, blocked, and zombie is
being initialized by using queue_create(), which is a call-in function from our
queue.c file. Inside this helper function, we are also initializing the stack,
assigning the thread “tid -> 0”, and putting the thread state as RUNNING. Also,
we are keeping track of the current thread by using the global variables
“current_thread” and “next_t_num”. The helper function finalizes by updating the
thread number by one (next_t_num + 1). Then the uthread_create() function
continues by doing the same instructions that the helper function does and is
finalized by returning the current thread ID.

Continuing with the uthread_yield() function. Here, we are context switching
from the current thread to a new thread. So basically, is passing a copy of its
data to a new thread. Next, in the uthread_self() function all it does is
returning the currently running thread TID. Next, the uthread_join() function
just executes an infinite loop where the loop breaks if “there are no more
threads that are ready to run in the system”(p1, prompt) and then returns.
Otherwise, we “simply yield to the next available thread” (p1, prompt) by
calling this function uthread_yield() and then returning “retval.” Finally, the
uthread_exit() function saves the return value of the current thread and then
sets the current thread state to zombie and then calls in uthread_yield()
function to do thread context switching to a new thread.

###### Resources used in phase 2:
* [GeeksForGeeks Enum] - How to use enum for enumeration of the thread's status
* [pthread_exit] - Understanding the purpose of the pthread_exit function
* [pthread_join] - Understanding the functionality of pthread_join

### Phase 3: Uthread Join

In this phase, we are programming a proper behavior of the uthread_join()
function. In other words, this means that we are implementing the data structure
that is called thread control block or TCB.

We mainly work with this function, but also we created helper functions such as
iterate_find() and iterate_helper(), and a global static integer and enum.

According to the prompt (section 5.4), when the first thread “T1” joins another
thread “T2”, there are two possible cases that can occur. We programmed for
these two scenarios, so when the “T2”(child) is still active, then the
T1(parent) must be blocked until the T2(child) dies. In addition, when “T2 dies,
then T1 is unblocked and collects T2.” The other case is for when if “T2 is
already dead then T1(parent) can collect T2 (child) immediately.” This is the
same as saying that the unblocked parent collects the unblocked child, then we
free the dead child. So this is what is happening in our uthread_join()
function.

We used the helper function of iterate_find() to find the thread ID of the
current thread. To do this, inside this function, we do a call in function using
queue_iterate() (that is in the queue.c file) to help us find the thread for
when is in the ready, blocked or zombie state. The iterate_helper() function
mostly serves to debug and test our code.

###### Resources used in phase 3:
* [pthread_join] - understanding pthread join function further

### Phase 4: Preemption
Phase four began with an emence ammount of research in order to fully understand
the preemetion process. Resource 1 gave insight into two essential aspects of
phase 4: the signal handling and the timer configuration. Cross-refrencing this
resource to the two resources provided in section 5.5.1 allowed for a complete
understanding of the roles of each aspect. The signal handler described by the
prompt was to perform a yielding action on the threads, which was part of phase
two. Because of this, the signal handler we implemented was just a call to
uthread_yield. The provided blocking and unblocking manual gave a framework for
using a global sigset_t variable as a controller.
###### Resources used in phase 4:
* [Informit] - How to use setitimerfor sig alarm
* [GNU Signal Actions] - Understanding handlers
* [GNU Setting an Alarm] - Working with itimerval
* [GNU Blocking Signals] - How to use sigprocmask for blocking/unblocking

  [pthread_join]: <http://man7.org/linux/man-pages/man3/pthread_join.3.html>
  [pthread_exit]: <http://man7.org/linux/man-pages/man3/pthread_exit.3.html>
  [Linked Lists]: <https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/tutorial/>
  [GeeksForGeeks Delete Node]: <https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/>
  [GeeksForGeeks Enum]: <https://www.geeksforgeeks.org/enumeration-enum-c/>
  [GNU Blocking Signals]: <https://www.gnu.org/software/libc/manual/html_mono/libc.html#Blocking-Signals>
  [Informit]: <http://www.informit.com/articlesarticle.aspx?p=23618&seqNum=14>
  [GNU Signal Actions]: <https://www.gnu.org/software/libc/manual/html_mono/libc.html#Signal-Actions>
  [GNU Setting an Alarm]: <https://www.gnu.org/software/libc/manual/html_mono/libc.html#Setting-an-Alarm>
