#include <signal.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <string.h>

#include "preempt.h"
#include "uthread.h"

/*
 * sigset_t represents a signal set.
 * All signal blocking functions use signal set to specify
 * what signals are efected
 */
sigset_t block_sig;
/*
 * Frequency of preemption
 * 100Hz is 100 times per second
 */
#define HZ 100

//Block or unblock signals by modifying signal mask
void preempt_disable(void)
{
  if(sigprocmask(SIG_BLOCK, &block_sig, NULL) == -1){
    exit(1);
  }
}

void preempt_enable(void)
{
  if(sigprocmask(SIG_UNBLOCK, &block_sig, NULL) == -1){
    exit(1);
  }
}

/*
force the currently running thread to yield, so that another thread can be scheduled instead.
*/
void yield_handler(int signum){
  uthread_yield(); //completed function from uthread.c
}


/*
use setitimer
a generalization of alarm call
schedules deliv of a sig after a fixed ammt of time
*/
void preempt_start(void)
{

  /*
  sigaction
  more information that the signal function
  sa_handler - pointer to function
  */
  struct sigaction sig_act;

  /*
  itimerval
  it_value    - time until next timer expires and sig is sent
  it_interval - value reset to after it expires, if 0 timer will be disabled after it expires.
   */
  struct itimerval timer;

  // init signal
  sigemptyset (&block_sig); //exclude al defined signals
  sigaddset (&block_sig, SIGVTALRM); //add signal to signal set block_sig only modifies block_sig

  //install signal handler for SIGVTALRM
  memset (&sig_act, 0, sizeof (sig_act));

  //make the signal handler call uthread_yield
  sig_act.sa_handler = yield_handler;
  if (sigaction (SIGVTALRM, &sig_act, NULL) == -1){
    exit(1);
  }

  timer.it_interval.tv_usec = 1000000/HZ; //1000000/100Hz = 1/100Sec
  timer.it_interval.tv_sec = 0;

  timer.it_value.tv_usec = 1000000/HZ;
  timer.it_value.tv_sec = 0;

  //returns -1 if fails
  if (setitimer(ITIMER_VIRTUAL, &timer, NULL) == -1){
    exit(1);
  };
}
