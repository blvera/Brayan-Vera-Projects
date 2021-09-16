#  Program created by Brayan Vera. Date 07/03/21

#  Program name: Merge_Two_Sorted_Array
#  This program gets two sorted arrays and merges them in ascending order.
#  Example:
#  [1,2,3] and [2,3,4] = [1,2,2,3,4]
#  [] and [1,2,3,4] = [1,2,3,4]
#  [] and [] = []
#  [1,40,60,300] and [4,5,6,80] = [1,4,5,40,60,80,300]

#  What to do next:
#  Try this is object oriented program in "linked list" form. (in progress)

def merge_two_sorted_lists(l1,l2):

    new_list = []
    counter = 0
    check_loop = 0

    if len(l1) == 0:
        print("returning: {}".format(l2))
        return l2
    if len(l2) == 0:
        print("returning: {}".format(l1))
        return l1

    for first_val_l1 in l1:
        if first_val_l1 == l2[counter]:
            new_list.append(first_val_l1)
            new_list.append(l2[counter])
        elif first_val_l1 < l2[counter]:
            new_list.append(first_val_l1)
            new_list.append(l2[counter])
        elif first_val_l1 > l2[counter]:
            new_list.append(l2[counter])
            new_list.append(first_val_l1)
        counter += 1

    while len(l1) != check_loop:
        counter = 0
        for swap_val in new_list:
            counter += 1
            if swap_val > new_list[counter]:
                new_list[counter - 1], new_list[counter] = new_list[counter], new_list[counter - 1]
            if counter == len(new_list) - 1:
                counter -= 1
                #print("the final sorted list is  {}".format(new_list))

        check_loop += 1
    print("The combined sorted list is: {}".format(new_list))
    return new_list

def main():
    l1 = [1,40,60,300]
    l2 = [4,5,6,80]
    merge_two_sorted_lists(l1,l2)

if __name__ == "__main__":
    main()


