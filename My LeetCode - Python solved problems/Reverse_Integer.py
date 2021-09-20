#  Program created by Brayan Vera. Date 08/17/21

#  Program name: Reverse_Integer
#  This program reverses the user's integer, no matter if is negative.
#  This program only accepts 32 bit numbers.
#  Example:
#  123456          =  654321
#  -23453          =  -35432
#  0               =  0
#  123             =  321
#  -123            =  -321
#  16545435435139  = 0
#  -16545435435139 = 0
def reverse_integer(x):
    int_to_str = str(x)

    #splits the string every n = 1 character with a comma
    n = 1
    split_string = [int_to_str[index: index + n] for index in range(0, len(int_to_str), n)]
    #print(split_string)

    new_reversed_list = []

    #stores the - in the initial position of the new string
    if split_string[0] == "-":
        the_minus = split_string.pop(0)
        new_reversed_list.append(the_minus)

    # Loops as many times there are numbers in the string each is stored in a new list.
    # Also, it stores the last element in a new list, then it keeps adding in to the stack.
    while len(split_string) > 0:
        last_out = split_string.pop()
        new_reversed_list.append(last_out)
        #print("the reversed number", new_reversed_list)

    # Takes out the comma between each value in the list.
    num_nocomma = ''.join(new_reversed_list)
    convert_str_to_num = int(num_nocomma)
    #print("printing the answer",convert_str_to_num)

    # Taking care to deal wil 32 bit numbers only
    if convert_str_to_num > 2147483641 or convert_str_to_num < -2147483641:
        print("Value is not under 32 bits, please enter value again.")
        return 0

    print(convert_str_to_num)
    return convert_str_to_num

def main():
    x = -214
    reverse_integer(x)

if __name__ == "__main__":
    main()