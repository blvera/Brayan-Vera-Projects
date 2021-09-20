#  Program created by Brayan Vera. Date 07/12/21

#  Program name: Palindrome_Num_Identifier
#  -This program makes sure to accept only palindrome numbers.
#  -This means the number that is the same as reversed.
#  -This program returns True if palindrome number is entered,
#   returns False otherwise.
#  -This program does not accept negative numbers.
#  -Thisprogram does not accept strings.
#  Example:
#  121     is good = True
#  12321   is good = True
#  122221  is good = True
#  1211121 is good = True
#  2222    is good = True
#  1221    is good = True
#  -121    not valid = False

#  Found another technique:
#  -This program does not follow this technique, but we can also check last digit and first digit
#   incrementing and decrementing the indexes until we reach the middle and stop the program.

#  The way this program operates is by storing the input in a list that separates each digit
#  Then another list in reverse is created and in the end is compared to see if is a palindrome.
def palindrome_check(x):
    # Makes sure to not accept strings.
    if isinstance(x,str) == True:
        print("Invalid input, only numbers please, no string.")
        return False
    # Makes sure does not accept negative numbers.
    if x < 0:
        print("Not valid, only possitive numbers please.")
        return False

    # Conversts the number to a string.
    int_to_str = str(x)
    # To split each number value individually and placed them into a list.
    n = 1
    split_string = [int_to_str[index: index + n] for index in range(0, len(int_to_str), n)]
    #print("The first string: {}".format(split_string))

    # Creating a new list to store the given list before it disappears when poping.
    store_old_str = []
    for store_old in split_string:
        store_old_str.append(store_old)

    new_list = []
    # Used to pop the last value of the old list and storing it into a new list.
    while len(split_string) != 0:
        last_val_pop = split_string.pop()
        new_list.append(last_val_pop)
        #print("The new list: {}".format(new_list))

    #print("The old string is : {}".format(store_old_str))
    #print("The new reversed string is : {}".format(new_list))

    if store_old_str == new_list:
        print("Is a palindrome.")
        return True
    else:
        print("Is not a palindrome.")
        return False

def main():
    x = 155545         #Enter number here. 
    palindrome_check(x)

if __name__ == "__main__":
    main()

