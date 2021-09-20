#  Program created by Brayan Vera. Date 09/01/21

#  Program name: Search_Num_Insert_Index
#  This program deals with a sorted list.
#  This program searches in a list the index where it can insert the user's number,
#  and outputs the index value where that number can be inserted.
#  Example:
#  [1,2,3,4,5,6] and insert 3 = 2  <--because 3 can be inserted at index 2.
#  [1,3,6,8,9] and insert 7 = 3  <--becasuse 7 can be inserted at index 3, and is btw 6 and 8.
#  [1,2,4,5,6] and insert -39 = 0

def search_insert_position(nums, insert):

    count_position = 0
    for check_num in nums:
        if check_num == insert:
            print("The index position is :",count_position)
            return count_position

        if check_num > insert:
            print("The index position is :", count_position)
            return count_position

        count_position += 1
    print(count_position)
    return count_position

def main():
    nums = [1, 3, 5, 6,7,34,56,80]    #<---Change to your list of numbers HERE.
    insert = 30                       #<---Enter the number you want to find its insertion index
    search_insert_position(nums, insert)

if __name__ == "__main__":
    main()