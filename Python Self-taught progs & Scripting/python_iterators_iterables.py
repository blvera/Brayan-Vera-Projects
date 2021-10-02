#  Program created by Brayan Vera. Date 09/15/21

#  Program name: python_iterators_iterables
#  We can loop over tuples, dictionaries, strings, files, generators and other objects.

#  ITERABLES are not the same as iterators.
#  -A list is iterable but is not an iterator.
#  -Something that is iterable is something that can be looped over.
#  -Example: list is iterable
#  How can we tell something is iterable?
#  -If something is iterable, it needs to have the special method of __iter__
#   -To do this, we can print(dir(nums)) and would output a lot of methods, but we looks if it has __iter__

#  ITERATOR is an object with a state, so that it remembers where it is during iteration.
#  -Iterators also know how to get their next value with the __next__ method
#  -Example: list does not have a __next__ method. list does not have a state, does not know how to get their next value.
#            Therefore a list is not an iterator



def main():

    nums = [1,2,3]
    #print(dir(nums)) #It does have the method __iter__ meaning that is iterable.

    i_nums = iter(nums) # Making an iterator. Inside, it had the method __next__
    #print(i_nums)       # This tells me that it is an iterator
    #print(dir(i_nums))  # This gives me all the methods that correspond, and we see that it has __next__ 
    print(next(i_nums)) # To get the first item in te list. And remembers where it is.
    print(next(i_nums)) # To get the following next item in the list.
    # To make the loop stop by itelf when it goes out of bound when trying to get all numbers
    while True:
        try:
            item = next(i_nums)
            print(item)
        except StopIteration:
            break
if __name__ == "__main__":
    main()