#  Program created by Brayan Vera. Date 09/09/21

#  Program name:  Roman_To_Integer
#  This program converts roman numbers into integers.
#  This program accepts valid roman numbers only. (pending)
#  Enter value in the main() function below.
#  Example
#  XXX    = 30
#  IX     = 9
#  XC     = 90
#  DCCCLX = 860
#  I consider this to be a brute force programming program. But I can now improve it (pending).
#  Things I can do to improve the code is the use of: List comprehensions, Dictionary comprehension and more.
def roman_to_num(s):

    add_num = 0
    index = 0
    result = 0
    check_len = 0

    if s[index] == "I":
        add_num += 1
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index+1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "V":
                add_num += 3
                result = add_num
            elif next_digit == "X":
                add_num += 8
                result = add_num
            # check len here
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "V":
        add_num += 5
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "X":
        add_num += 10
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "X":
                if s[check_len - 2] == "I":
                    add_num += 8
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 10
                result = add_num
            elif next_digit == "L":
                if s[check_len - 2] == "X" and check_len == len(s):
                    add_num += 30
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 30
                result = add_num #could make it like the previus if

            elif next_digit == "V":
                if s[check_len - 2] == "I":
                    add_num += 3
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 5
                result = add_num
            elif next_digit == "C":
                add_num += 80
                result = add_num
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "L":
        add_num += 50
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "V":
                if s[check_len - 2] == "I":
                    add_num += 3
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 5
                result = add_num
            elif next_digit == "X":
                if s[check_len - 2] == "I":
                    add_num += 8
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 10
                result = add_num
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "C":
        add_num += 100
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "V":
                if s[check_len - 2] == "I":
                    add_num += 3
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 5
                result = add_num
            elif next_digit == "X":
                if s[check_len - 2] == "I":
                    add_num += 8
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 10
                result = add_num
            elif next_digit == "L":
                if s[check_len - 2] == "X": #and check_len == len(s)
                    add_num += 30
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 50
                result = add_num
            elif next_digit == "D":
                if s[check_len - 2] == "C" and check_len == len(s):
                    add_num += 300
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 300
                result = add_num
            elif next_digit == "C":
                if s[check_len - 2] == "X":
                    add_num += 80
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 100
                result = add_num
            elif next_digit == "M":
                if s[check_len - 2] == "C":
                    add_num += 800
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "D":
        add_num += 500
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1

            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "V":
                if s[check_len - 2] == "I":
                    add_num += 3
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 5
                result = add_num
            elif next_digit == "X":
                if s[check_len - 2] == "I":
                    add_num += 8
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 10
                result = add_num
            elif next_digit == "L":
                if s[check_len - 2] == "X": #and check_len == len(s)
                    add_num += 30
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 50
                result = add_num
            elif next_digit == "M":
                if s[check_len - 2] == "C" and check_len == len(s):
                    add_num += 300
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 300
                result = add_num
            elif next_digit == "C":
                if s[check_len - 2] == "X":
                    add_num += 80
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 100
                result = add_num
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

    elif s[index] == "M":
        add_num += 1000
        result = add_num
        check_len += 1
        if check_len == len(s):
            print("The '{}' roman number converts to the integer: {}".format(s,result))
            return result
        for next_digit in s[index + 1:]:
            check_len += 1
            if next_digit == "I":
                add_num += 1
                result = add_num
            elif next_digit == "V":
                if s[check_len - 2] == "I":
                    add_num += 3
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 5
                result = add_num
            elif next_digit == "X":
                if s[check_len - 2] == "I":
                    add_num += 8
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                add_num += 10
                result = add_num
            elif next_digit == "L":
                if s[check_len - 2] == "X": #and check_len == len(s)
                    add_num += 30
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 50
                result = add_num
            elif next_digit == "C":
                if s[check_len - 2] == "X":
                    add_num += 80
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 100
                result = add_num
            elif next_digit == "D":
                if s[check_len - 2] == "C":
                    add_num += 300
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 500
                result = add_num
            elif next_digit == "M":
                if s[check_len - 2] == "C":
                    add_num += 800
                    result = add_num
                    if check_len == len(s):
                        print("The '{}' roman number converts to the integer: {}".format(s,result))
                        return result
                    continue
                add_num += 1000
                result = add_num
            if check_len == len(s):
                print("The '{}' roman number converts to the integer: {}".format(s,result))
                return result

def main():
    s = "XXX"  #<------Enter Roman number HERE
    roman_to_num(s)

if __name__ == "__main__":
    main()
# I    = 1
# III  = 3
# IV   = 4
# V    = 5
# VIII = 8
# X    = 10
# XL   = 40
# L    = 50
# XC   = 90
# C    = 100
# D    = 500
# M    = 1000
