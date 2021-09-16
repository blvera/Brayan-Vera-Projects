#  Program created by Brayan Vera. Date 09/06/21

#  Program name: Two_Sum
#  This program gets a list and a target number.
#  The program searches for two values in the list that add up to the target number.
#  The output are the indexes of the two numbers found in the list.

#  Example:
#  Input: nums = [2,7,11,15], target = 9
#  Output: [0,1]
#  Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#  Input: nums = [3,2,4], target = 6
#  Output: [1,2]

#  Input: nums = [3,3], target = 6
#  Output: [0,1]
def two_sum(nums, target):

    index = []
    count_i = 0
    i_index = 0
    j_index = 0
    #print("this is the len of nums:",len(nums))
    for i in nums:
        count_i += 1
        #print("this is i: {}".format(i))
        j_index = count_i
        for j in nums[count_i:]:
            #print("this is j: {} with [{},{}]".format(j,i_index,j_index))
            #print(count_i)
            if (i + j) == target:
                #print("it got in")
                index.append(i_index)
                index.append(j_index)
                print("index: {}".format(index))
                return index
            #print("j_index is: ",j_index)

            j_index += 1
            #print(">>>>before j: {}".format(j_index))
            #print(">>>>after j: {}".format(j_index))
        i_index += 1


def main():
    nums = [2,5,5,11]    #<--Enter your desire list here
    target = 10          #<--Enter the target number
    two_sum(nums,target)

if __name__ == "__main__":
    main()
