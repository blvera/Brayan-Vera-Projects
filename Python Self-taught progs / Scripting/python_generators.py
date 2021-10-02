#  Program created by Brayan Vera. Date 09/10/21

#  Program name: python_generators
#  -This Program will show an overview of what generators are in python.
#  -It will show how the use of generators are better than lists.
#  Generators do not hold entire result in memory
#  Yield waits to be asked to provide value.
#  Generators prevents unnecesary storage and running
#  Generators have the advantage in terms of performance in the way of not putting values into memory.
#  Squaring numbers using a list

#import mem_profile
import random
import time

def square_nums_list(nums):

    my_list = []
    for val in nums:
        my_list.append(val*val)
    #print(my_list)
    return my_list

# Squaring numbers using a generator bc is much more readable.
def square_nums_generator(nums):
    for val in nums:  
        yield (val*val) #yield one result at a time, waits to be ask to provide value


#Mmory condumption is more here because list gets all the values inside.
def people_list(names,majors,people_number):
    result = []
    for i in range(people_number):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

# Memory consumption is less here
# because the generator hold the value and does not store everything like the list.
# Memory is alsmost the same as it was before this function got to run.
def people_generator(names,majors,people_number):
    for i in range(people_number):
        #using a dictionary
        person = {
                    'id': i,                       #giving it an id
                    'name': random.choice(names),  #giving it random from a list of names
                    'major': random.choice(majors) #giving it random from a list of majors
                }
        yield person


def main():
    nums = [1,2,3,4,5]
    square_nums_list(nums)
    square_nums_generator(nums)
    #print(square_nums_generator(nums)) #is a generator, will not print numbers.
    #print(next(square_nums_generator(nums))) #to obtain the first val from yield.
    #print(list(square_nums_generator(nums))) #To obtain the values in a list.

    # Generator in a list comprehension way. Note: having it in parenthesis.
    my_nums = (i*i for i in nums)
    #print (my_nums)  #This prints a generator


    #UNCOMENT FROM THIS LINE DOWN TO SEE that
    # names = ['Mathias','Carol','Clark','Hugo','Ricky','Jimmy']
    # majors = ['Mathematics','Chemistry','Physics','Art','Architecture','Programming']
    # people_number = 1000000
    # people_list(names,majors,people_number)
    # people_generator(names,majors,people_number)

    # t1 = time.clock()
    # people = people_list(people_number)
    # t2 = time.clock()

    # # t1 = time.clock()
    # # people = people_generator(people_number)
    # # t2 = time.clock()

    # print(f'Memory (After): {mem_profile.memory_usage()}Mb')
    # print(f'Took {t2-t1} Seconds')


if __name__ == "__main__":
    main()