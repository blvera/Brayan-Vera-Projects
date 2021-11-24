

def twosum(nums,target):


    sum_dict = {}

    # The loop will subtract first then it will look for the key that equals to
    # the subtracted number
    for i,num in enumerate(nums):  #[4,2,7,8,15] , target = 9
        if num in sum_dict:
            print(sum_dict[num], i)
            #returning the key value and current index
            return [sum_dict[num], i]

        #adding key values to the dictionary
        else:
            sum_dict[target-num] = i
            #          9 - 4  (5) = 0

    #if it does not find it, return nothing
    return []



def main():

    nums= [2,7,11,15]
    target = 9
    twosum(nums,target)

if __name__ == "__main__":
    main()