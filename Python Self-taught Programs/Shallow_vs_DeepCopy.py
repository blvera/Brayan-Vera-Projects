#Created by Brayan Vera. Date Sep 8, 2021
#Understanding the difference between "Shallow Copy" and "Deep Copy"

import copy
#Both list point to the same memory address
# list1 = [1,2,3,4,5]
# list2 = list1

# print (list1)
# print (list2)


#Doing Shallow copy
#list1 = [1,2,3,4,5]
#list2 = list1.copy()  #<---adding the .copy() makes it a SHALLOW COPY which also assigns a different memory allocation.

def shallow_copy():
    list1 = [[1,2,3,4],[5,6,7,8]]
    list2 = list1.copy() #doing shallow copy here

    list1.append([40,50,60,70])
    print (list1)
    print (list2) #This will remain the same. It will not print the appended list to list1
    #It will only print the same, if we are making changes inside the list1

def deep_copy():
    list1 = [1,2,3,4]
    list2 = copy.deepcopy(list1) #creates a different memory allocation || only will update this.
    list1[0] = 90

    print (list1)
    print (list2)


def main():

    #shallow_copy()
    deep_copy()


if __name__ == "__main__":
    main()


