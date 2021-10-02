#Created by Brayan Vera. Date Sep 9, 2021
#These are various list comprehension examples that I have created to better
#understand its behavior

#The usual way of passing list values to other list
def usual_way():
    list1 = [1,2,3,4,5]
    list2 = []
    for n in list1:
        list2.append(n)
    print(list2)

#List comprehension way.
def list_comprehension():
    list1 = [1,2,3,4,5,6]
    list2 = [n for n in list1] #The first n is what we are appending to our list.
    print(list2)

#Returning squared elements in the list
def squared_list_comprehension():
    list1 = [1,2,3,4,5,6,7]
    list2 = [n*n for n in list1] #The first n is what we are appending to our list.
    print(list2)

#Returning only even numbers
def even_list_comprehension():
    list1 = [1,2,3,4,5,6,7,8]
    list2 = [n for n in list1 if n % 2 == 0] #having the if condition towards the end.
    print(list2)

#I want for each letter in 'abcd' to return the sequence of '0123'.
# That means that for example: ('a',0)('a',1)('a',2)('a',3)

def sequence_of_letter_and_num():
    new_list = []
    for letter in 'abcd':
        for num in range(4): #<--This will iterate 0,1,2,3
            new_list.append((letter,num))
    print(new_list)

def seq_letter_num_list_comprehension():

    new_list = [(letter,num) for letter in 'abcd' for num in range(4)] #The second for loop becomes the nested loop.
    print(new_list)
    #output:
    #[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

#I want dict{'name':'hero'}
def dictionary():
    names = ['Bruce','Filip','Andrew','Santiago','Richard']
    heros = ['Batman','Superman','Aquaman','Spiderman','Sonic']
    dict = {}
    #name is key and hero is the value.
    for name, hero in zip(names,heros):
        dict[name] = hero  #<--Assign name to corresponding hero in dictionary
    print(dict)
    #output:
    #{'Bruce': 'Batman', 'Filip': 'Superman', 'Andrew': 'Aquaman', 'Santiago': 'Spiderman', 'Richard': 'Sonic'}

def dictionary_comprehension_way():
    names = ['Bruce','Filip','Andrew','Santiago','Richard']
    heros = ['Batman','Superman','Aquaman','Spiderman','Sonic']
    #dict = {name:hero for name,hero in zip(names,heros)} #<--The dictionary comprehension way.
    #In the case not wanting Andrew to be added
    dict = {name:hero for name,hero in zip(names,heros) if name != 'Andrew'}
    print(dict)

#A set is like a list but it has all unique values
#meaning that it excludes duplicates
def set_way():
    nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,9]
    new_set = set()
    for n in nums:
        new_set.add(n)
    print (new_set)

def set_way_comprehension():
    nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,9]
    new_set = set(n for n in nums)  #The set comprehension way.
    other_set = {n for n in nums} #Tuple set? comprehension way
    print("new_set: {}".format(new_set))
    print("other set: {}".format(other_set))

#Generator expression
def generator_func():
    nums = [1,2,3,4,5,6,7,8,9]
    for n in nums:
        yield n*n  #This yield remembers all the values that its being passed.

def generator_expression_func():
    nums = [1,2,3,4,5,6,7,8,9]
    my_gen = (n*n for n in nums)
    for i in my_gen:
        print (i)



def main():

    #usual_way()
    #list_comprehension()
    #squared_list_comprehension()
    #even_list_comprehension()
    #sequence_of_letter_and_num()
    #seq_letter_num_list_comprehension()
    #dictionary()
    #dictionary_comprehension_way()
    #set_way()
    #set_way_comprehension()
    # generator_func()
    # my_gen = generator_func()
    # for i in my_gen:
    #     print(i)
    generator_expression_func()

if __name__ == "__main__":
    main()
