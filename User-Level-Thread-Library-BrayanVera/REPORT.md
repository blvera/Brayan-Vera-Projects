# ECS 150: Project #3 - User-level thread library (part 2)

## REPORT

### Part 1: semaphore API
We started this project by reading the project3.html file first and at the same time reading the sem.h API file. That allowed us to get a better idea about what we have to do, so then we began programming project 3.

In the sem.c file, we did the programming function by function. First, we started by writing the data structure “semaphore.” In that structure, we initialize the out “count” (that we will be using throughout the code) and our “queue” (named as queueWait).
Then we went working on the next function “sem_create”(creating multiple semaphores). Inside, we just allocated space for the new semaphore and then just created a new queue under the “newSem” variable. Then, we returned the pointer to the initialized semaphore.

For the destroy function, we dealt with entering and exiting the critical section to handle error checking. So this means, whenever the “sem” is NULL or the sem “count” has not been initialized, then return -1. Then we again exited critical selection, but we first destroyed our “queue” and freed our “sem”.

For the implementation of our down and up functions, we take care of the returning value errors at first. Then for the “down function”, we had a while loop to check for the case of taking unavailable semaphores and then blocking the thread when it happens. Then, we update the buffer by decreasing the count number, and we finalize by exiting the critical section. Moreover, for the “up function” is taking care of whenever the queue size of “queueWait” is greater than 0, then we deallocate first, to then block our current thread. 

Then, we incremented our count to indicate that there was something added to the buffer, and we exit critical section at the end.

Lastly, for the sem_getvalue function, we first did with the error cases, for then do if statements to assign “internal count to the data item” when the “sem” count is greater than 0, and also to “assign a negative number” for the count of the threads that are currently blocked.

To make sure our sem.c code was working, we constantly debugged it. Then we checked it with the tester files given to us. We got good results which indicate that we were done with the semaphore file. We asked if it was necessary for us to make our own tester for the semaphore file, but ta’s and tutors told us that the tester files are given already cover pretty much everything.
###### Resources used in phase 1:
* https://www.geeksforgeeks.org/semaphores-operating-system/ -> Used for undrstanding the concept of semaphore better. Referencing the images inside to have a better vizualitation of semaphores.

### Part 2: TPS API

We started programming this file by first reading the tps.h API and the 
instructions .html file. After this we were able to think about what to do
first. So we started having a data structure that initializes the our thread tid 
and our memory address. But later after doing the tps_read and then tps_write,
we noticed that we needed to have another data structure that can take care of 
our page thread and memory address.  We have tps_find, page_find and tps_init
where we used queue_iterate to search for our tps and then to find the tsp.  The 
function tps_create, we pretty much started by making a newtps (with nothing in
it). Then, we get the “tid” using pthread_self(). After that, we iterate
throught the tps queue, and then if there is a tps that has the same “tid” is
going to return -1. Then we allocate space for the new tps. Then, we passed the
tid, and then also the page and the reference. The we just put it to queue and
exit the critical section. 

For the next function tps_destroy, we get the tid using the pthread_self and
then we initialize a new tps, and then we enter the critical section. Then we
iterate on the tps queue to find the “tps” using the tid. Then, we free the
tps-> page, then after that we delete the queue (deallocate). In the end, we
exit the critical section and returned 0.

For the tps_read we finished it completely according to our logic and by
referencing it to the API. However, for the tps_write and the tps_clone, we had
many problems and then we did not have time to debug our code. Then, we tested
the tester tps.x file, and it did not work - sadly.

###### Resources used in phase 2:
* http://man7.org/linux/man-pages//man2/munmap.2.html 
  -> Used for knowing what to put inside mmap.(to understand map better)
* https://linux.die.net/man/2/mprotect   
  -> used to understand the read and write functions better (was provided in the instructions).


