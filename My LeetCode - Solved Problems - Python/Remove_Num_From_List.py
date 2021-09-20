#  Program created by Brayan Vera. Date 08/02/21

#  Program name: Remove_Element_From_Array
#  This program receives a number and removes all similar numbers from a list.
#  If number entered is not in the list, then it does not remove anything.
#  Example:
#  [1,2,2,2,3,4,5,6] and remove 2 = [1,3,4,5,6] <-- 2 is removed from this list.
#  [1,2,3,4,5] and remove 10 = [1,2,3,4,5] <-- The list stays the same, 10 not found in list.
#  []

def remove_element(nums, val):

    remove_index = 0
    for remove_num in nums[remove_index:]:
        if remove_num == val:
            popping = nums.pop(remove_index)
            #print("number popping: {}".format(popping))
            continue
        remove_index += 1
    print("The final list consist of: {}".format(nums))
    return nums

def main():
    nums = [3,2,2,3]  #Enter the list of numbers of your preference HERE.
    val = 4           #Enter the value you wan to remove from the list.
    remove_element(nums, val)

if __name__ == "__main__":
    main()