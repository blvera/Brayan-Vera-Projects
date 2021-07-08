//Tutor Sean Help

#include <stddef.h>
#include <stdlib.h>

#include "queue.h"
#include "sem.h"
#include "thread.h"

struct semaphore {
	size_t count;  
	queue_t queueWait;
};

sem_t sem_create(size_t count)
{
	sem_t newSem = (sem_t) malloc(sizeof(struct semaphore));
	newSem->count = count;
	newSem->queueWait = queue_create();
	
	if (newSem == NULL || newSem->queueWait == NULL){
		return NULL;
	}
	
	return newSem;
}

int sem_destroy(sem_t sem)
{
	enter_critical_section();
	if (sem == NULL || sem->count <= 0){
		exit_critical_section();
		return -1;
	}
	queue_destroy(sem->queueWait);
	free(sem);
	return 0;
	exit_critical_section();
}

int sem_down(sem_t sem)
{
	enter_critical_section();
	if (sem == NULL){
		exit_critical_section();
		return -1;
	}

	while (sem->count == 0) { //whenever a process wait, it continuouslly checks for a semaphore value
		//malooc
		pthread_t tid = pthread_self(); //getting the id

		queue_enqueue(sem->queueWait, &tid);  //have to enqueue before blocking
		thread_block(); //blocking
	}

  	sem->count -= 1;   //upadintg buffer
	exit_critical_section();
	return 0; //if semaphore was successfully taken
}

int sem_up(sem_t sem)
{
/* TODO Phase 1 */
	enter_critical_section();
	if (sem == NULL){
		exit_critical_section();
  	return -1;
  	}

	pthread_t *tid;
	if (queue_length(sem->queueWait) > 0){
		queue_dequeue(sem->queueWait, (void **)&tid);  //have to deque, then unblock
		thread_unblock(*tid);

	}
							//else if {  //if length of queue is not greater than 0.
	sem->count += 1; //updating buffer. item added to the buffer

	exit_critical_section();
	return 0;
}

int sem_getvalue(sem_t sem, int *sval)
{
	enter_critical_section();
	if (sem == NULL || sval == NULL){
		exit_critical_section();
		return -1;
	}
	
	if (sem->count == 0){
		*sval = sem->count * -1; 
	}
	else if (sem->count > 0){
		*sval = sem->count;
	}
	exit_critical_section();
	return 0;
}

