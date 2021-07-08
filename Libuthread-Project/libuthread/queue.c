#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "queue.h"


struct ele {
  struct ele *next;
  void *data;
};

struct queue {
  struct ele *first, *last;
  int len;
};



//init all struct conditions for an empty queue
queue_t queue_create(void)
{
  //allocate memory
  struct queue *queue = (struct queue*)malloc(sizeof(struct queue));
  //empty -> no first/last elements
  queue->last = NULL;
  queue->first = NULL;
  queue->len = 0;
  return queue;
}

int queue_destroy(queue_t queue)
{
  if(queue == NULL || queue->first != NULL){
    //queue doesnt exist or queue is no empty
    return -1;
  }
  else{
    //no elements -> deallocate all memory assosiated with queue
    free(queue);
    return 0;
  }
}

int queue_enqueue(queue_t queue, void *data)
{
  //check for valid args
  if (data == NULL || queue == NULL){
    return -1;
  }
  //allocate space for new element in queue
	struct ele *element = (struct ele *)malloc(sizeof(struct ele));
  //init element values
  element->data = data;
  element->next = NULL;
  //increase queue length keeper
  queue->len++;

  //check if first element
  if (queue->first == NULL){
    //first element -> first and last point to same element
    queue->last = element;
    queue->first = element;
  } else {
    //extend existing queue
    queue->last->next = element;
    queue->last = element;
  }
  return 0;
}

int queue_dequeue(queue_t queue, void **data)
{
  //check for valid arguments and elements
  if (queue->first == NULL || data == NULL || queue == NULL ){
    return -1;
  }
  //decrease queue length keeper
  queue->len--;
  //deque oldest item and store value to data
	//struct ele *temp = queue->first;
  *data = queue->first->data;
  queue->first = queue->first->next;
  //*data = temp->data;
  return 0;
}

int queue_delete(queue_t queue, void *data)
{
  //check for valid arguments and elements
  if (queue->first->data == NULL || data == NULL || queue == NULL){
    return -1;
  }

  struct ele *current = queue->first;
  struct ele *previous = NULL;

  if (queue->len <= 1){
    //Queue only has one element check if element is data
    if (queue->first->data == data){
      //value is found in only queue element
      queue->first->data = NULL;
      queue->first->next = NULL;
      queue->len--;
      return 0;
    } else {
      //value not in only queue element
      return 0;
    }
  } else {
    //Queue has more than one elements
    while(current->data != NULL && current->data != data){
      printf("current->data = %d and data = %d\n", *(int *)current->data, *(int *)data);
      previous = current;
      current = current->next;
    }
    if (current == NULL){
      //value not in the queue
      return -1;
    }
    else if (current->next == NULL && current->data == data){
      //value is the last element in the queue
      previous->next = NULL;
      queue->last = previous;
      free(current);
    }

    else if (current == queue->first){
      //value is the first element in the queue
      struct ele* temp = queue->first->next;
      free(queue->first);
      queue->first = temp;
    }
    else{
      //value is an element in the middle of queue
      current->data = current->next->data;
      if (current->next->next){
        struct ele* temp = current->next->next;
        free(current->next);
        current->next = temp;
      } else {
        free(current->next);
      }
    }
    //decrease queue length keeper
    queue->len--;
    return 0;
  }
}

int queue_iterate(queue_t queue, queue_func_t func, void *arg, void **data)
{
  //check for valid arguments
  if (queue == NULL || func == NULL){
    //NULL found
    return -1;
  }

  struct ele *temp = queue->first;
  int retval = 0; // 0 -> itterate, 1 -> stop prematurely
  while (temp != NULL && retval != 1)
  {
    retval = func(temp->data, arg);
    if (retval == 1){
      //stop itterations prematurely
      *data = temp->data;
    }
    temp = temp->next;
  }
  return 0;
}

int queue_length(queue_t queue)
{
	return queue->len;
}
