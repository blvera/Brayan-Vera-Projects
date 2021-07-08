#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>

#include <queue.h>


void test_create(void)
{
  printf("BEGIN test_create: \n");
  queue_t q;
  q = queue_create();
  assert(q != NULL);
  printf("END test_create: \n\n");
}

void test_queue_simple(void)
{
    printf("BEGIN test_queue_simple: \n");
    queue_t q;
    int data = 3, *ptr;
    int data1 = 111;
    int len = 0;
    q = queue_create();
    queue_enqueue(q, &data);
    queue_enqueue(q, &data1);
    len = queue_length(q);
    printf("queue length: %d\n", len);
    queue_dequeue(q, (void**)&ptr);
    //assert(ptr == &data);
    printf("dequeued: %d\n", *(int *)ptr);
    queue_dequeue(q, (void**)&ptr);
    printf("dequeued: %d\n", *(int *)ptr);
    queue_destroy(q);
    printf("END test_queue_simple: \n\n");
}

void test_queue_adv(void)
{
    printf("BEGIN test_queue_adv: \n");
    queue_t q;
    int data = 3; // *ptr;
    int data1 = 67;
    int data2 = 10;
    int data3 = 9;
    int data4 =14;
    q = queue_create();
    queue_enqueue(q, &data);
    queue_enqueue(q, &data1);
    queue_enqueue(q, &data2);
    queue_delete(q, &data1);
    queue_enqueue(q, &data4);
    queue_enqueue(q, &data3);
    queue_delete(q, &data3);
    queue_delete(q, &data);
    queue_delete(q, &data2);
    queue_delete(q, &data4);
    queue_destroy(q);
    //assert(ptr == &data);
    printf("END test_queue_adv: \n\n");
}

void test_queue_null(void)
{
    printf("BEGIN test_queue_null: \n");
    queue_t q;
    //void data = NULL; // *ptr;
    q = queue_create();
    queue_enqueue(q, NULL);
    queue_enqueue(q, NULL);
    queue_destroy(q);
    printf("queue len %d\n",queue_length(q));
    //assert(ptr == &data);
    printf("END test_queue_null: \n\n");
}

static int inc_item(void *data, void *arg)
{
    int *a = (int*)data;
    int inc = (int)(long)arg;
    *a += inc;
    return 0;
}

/* Callback function that finds a certain item according to its value */
static int find_item(void *data, void *arg)
{
    printf("here\n");
    int *a = (int*)data;
    printf("a: %d\n", *a);
    int match = (int)(long)arg;
    printf("mathc: %d\n", match);

    if (*a == match)
    {
      printf("MATCH!\n");
      return 1;
    }


    return 0;
}

void test_iterator(void)
{
    queue_t q;
    int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int i;
    int *ptr;

    /* Initialize the queue and enqueue items */
    q = queue_create();
    for (i = 0; i < sizeof(data) / sizeof(data[0]); i++)
        queue_enqueue(q, &data[i]);

    /* Add value '1' to every item of the queue */
    queue_iterate(q, inc_item, (void*)1, NULL);
    assert(data[0] == 2);

    /* Find and get the item which is equal to value '5' */
    ptr = NULL;
    queue_iterate(q, find_item, (void*)5, (void**)&ptr);
    printf("PTR: %d\n", *ptr);
    assert(ptr != NULL);
    assert(*ptr == 5);
    assert(ptr == &data[3]);
}


int main(void){
  test_create();
  test_queue_simple();
  test_queue_adv();
  test_queue_null();
  test_iterator();
  printf("TEST COMPLETED\n");
  return 0;

}
