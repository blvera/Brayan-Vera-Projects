#  Program created by Brayan Vera. Date 07/22/21

#  Program name: Remove_Duplicate_Val_Sorted_Array
#  -This program does my own version of what the set() function does.
#  -This program looks for duplicate numbers and leaves only one copy.
#  -This program does not sort the values entered. But is something I can implement.
#  Example:
#  [1,2,3,4]         = [1,2,3,4]
#  [1,2,2,2,3,3,4,5] = [1,2,3,4,5]
#  []                = []
#  This program also supports unsorted array.
#  Example
#  [1,4,5,2,3,4,5,5] = [1,4,5,2,3]
def rem_dupli_sort_array(nums):

    new_list = []
    if len(nums) == 0 or len(nums) == 1:
        return nums

    for val in nums:
        if val not in new_list:
            new_list.append(val)
    print(new_list)
    return new_list

def main():
    nums = [1,4,5,2,3,4,5,5]
    rem_dupli_sort_array(nums)

if __name__ == "__main__":
    main()


#[1,2,3,3,3,3,3,4]   the output is  [1,2,3,4], with 4 values in it)
#[1]                 the output is  [1]  with 1 values in it