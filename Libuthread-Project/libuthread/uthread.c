#include <assert.h>
#include <signal.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "context.h"
#include "preempt.h"
#include "queue.h"
#include "uthread.h"




enum state {READY = 0, BLOCKED = 1 , RUNNING = 2, ZOMBIE = 3};

//Thread data structure definition
typedef struct {
    uthread_t tid;                   //thread id
    enum  state stateOfUthread;      //enum contect to call each // assign a starting value to ready .. in thread
    uthread_ctx_t CPU_Reg_Backup;    //register values
    void *stack;                     //reserved region of memory
    int ret;
    void *joined;
} thread_def;

// static thread_def iterate_find(uthread_t tid);
// static int iterate_helper(void *data, void *arg);


//GLOBALS
struct queue * ready;
struct queue * blocked;
struct queue * zombie;
uthread_t next_t_num = 0;      //increment as the number of threads grow
thread_def *current_thread;
thread_def *blocked_thread;

/*
 * function is to be called from the currently active and running thread in
 * order to yield for other threads to execute.
 */
void uthread_yield(void)
{

    //Dequeue next ready thread and elect to run
    thread_def *dequeued_thread;
    //Place current thread into propper queue
    switch(current_thread->stateOfUthread)
    {
      case ZOMBIE :
        //add to zombie queue
        queue_enqueue(zombie, current_thread);
        queue_dequeue(blocked, (void**)&blocked_thread); //cast to void pointer
        thread_def *temp_thread  = (thread_def *)malloc(sizeof(thread_def));
        temp_thread = current_thread;
        blocked_thread->stateOfUthread = RUNNING;
        current_thread = blocked_thread;

        uthread_ctx_switch(&temp_thread->CPU_Reg_Backup,&blocked_thread->CPU_Reg_Backup);
        return;
      case BLOCKED :
        //add to blocked queue
        queue_enqueue(blocked, current_thread);
        queue_dequeue(ready, (void**)&dequeued_thread); //cast to void pointer
      default:
        //state is running, should never be ready
        //demote from running to ready and add to ready queue
        current_thread->stateOfUthread = READY;
        queue_enqueue(ready, current_thread);
        queue_dequeue(ready, (void**)&dequeued_thread); //cast to void pointer
    }
    thread_def *current_copy = current_thread; //allows context switch after current = dequeued
    dequeued_thread->stateOfUthread = RUNNING;
    current_thread = dequeued_thread;

    //Context switch to update the newly dequeued threads registers
    uthread_ctx_switch(&current_copy->CPU_Reg_Backup, &dequeued_thread->CPU_Reg_Backup);
    return;
}


/*
 * Return the thread identifier of current thread
 */
uthread_t uthread_self(void)
{
    return current_thread->tid;
}


/*
 * Create thread 0 and init all struct fields
 * Init all queues for states
 */
static void thread_0(void)
{
    //Init queue states for READY, BLOCKED AND ZOMBIE. no need for Running
    ready = queue_create();
    blocked = queue_create();
    zombie = queue_create();
    //Init the main thread
    thread_def *thread_0 = (thread_def *)malloc(sizeof(thread_def));
    thread_0->stack = uthread_ctx_alloc_stack();  // init stack of size 32768
    thread_0->tid = next_t_num;                   // assign main thread tid 0
    thread_0->stateOfUthread = RUNNING;
    current_thread = thread_0; //current and only thread
    next_t_num++;
    return;
}


/*
 * Creates a new thread running the function to which
 * argument is passed, and returns the TID of this new thread.
 */
int uthread_create(uthread_func_t func, void *arg)
{
    if (next_t_num == 0)
    {
        thread_0(); //We must initilize the main thread
    }
    //allocate space for a new thread
    thread_def *new_thread = (thread_def *)malloc(sizeof(thread_def));
    new_thread->tid = next_t_num;
    new_thread->stateOfUthread = READY;
    new_thread->stack = uthread_ctx_alloc_stack();
    queue_enqueue(ready, new_thread);
    next_t_num++;
    /*
     *Initialize the stack and the execution context of the new thread
     *so that it  will run the specified function with the specified argument
     */
    uthread_ctx_init(&new_thread->CPU_Reg_Backup, &new_thread->stack, func, arg);
    return new_thread->tid;
}


void uthread_exit(int retval)
{
    current_thread->ret = retval;
    current_thread->stateOfUthread = ZOMBIE;
    uthread_yield();
}


static int iterate_helper(void *data, void *arg)
{
    int *a = (int*)data;
    thread_def *match = (thread_def*)(long)arg;
    uthread_t tid = match->tid;
    if (*a == tid)
    {
      return 1;
    }
    return 0;
}

static thread_def iterate_find(uthread_t tid)
{
  int intID = (int)tid;
  int *ptr=NULL;
  queue_iterate(ready, iterate_helper, &intID, (void**)&ptr);
  if (ptr != NULL)
  {
    return *((thread_def*)(long)ptr);
  }
  ptr = NULL;
  queue_iterate(blocked, iterate_helper, &intID, (void**)&ptr);
  if (ptr != NULL)
  {
    return *((thread_def*)(long)ptr);
  }

  ptr = NULL;
  queue_iterate(zombie, iterate_helper, &intID, (void**)&ptr);
  if (ptr != NULL)
  {
    return *((thread_def*)(long)ptr);
  }

  return *((thread_def*)(long)ptr);
}


int uthread_join(uthread_t tid, int *retval)
{
    if (tid == 0){
      return -1;
    }
    //check all queues for tid
    thread_def find = iterate_find(tid);
    thread_def *temp_thread = &find;
    thread_def *blocked_thread = (thread_def *)malloc(sizeof(thread_def));
    switch(temp_thread->stateOfUthread){
      case READY:
        current_thread->stateOfUthread = BLOCKED;
        blocked_thread = current_thread;
        queue_enqueue(blocked, blocked_thread);
        temp_thread->joined = current_thread;
        temp_thread -> stateOfUthread = RUNNING;
        current_thread = temp_thread;
        uthread_yield();


      case BLOCKED:
        current_thread->stateOfUthread = BLOCKED;
        blocked_thread = current_thread;
        queue_enqueue(blocked, blocked_thread);
        temp_thread->joined = current_thread;
        temp_thread -> stateOfUthread = RUNNING;
        current_thread = temp_thread;
        uthread_yield();

      case ZOMBIE:
        uthread_yield();
      case RUNNING:
        uthread_yield();
      default:
        return -1; //DELETE THIS TO MAKE UTHREAD RUN
    }
    return 0;
}
