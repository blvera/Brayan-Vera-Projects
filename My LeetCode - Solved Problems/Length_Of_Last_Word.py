#  Program created by Brayan Vera. Date 06/02/21

#  Program name: "Length_Of_Last_Word"
#  This program returns the length of the last word or number entered.
#  Blank spaces after last value are not counted.
#  Examples:
#  "Hello my name is Brayan" --> last value length: 6  b/c (Brayan has 6 letters)
#  "3      "                 --> last value length: 1  b/c (There is only 1 value)
#  "   Hello   "             --> last value length: 5  b/c (Hello has 5 letters)
#  "Hi my number is 12345"   --> last value length: 5  b/c (since 12345 are together and occupy 5 spaces)

def lengthOfLastWord(s):
    count = 0

    n = 1
    # To split each value individually and placed them into a list.
    split_string = [s[index: index + n] for index in range(0, len(s), n)]
    check_space = len(split_string) - 1

    # Start counting only when it reaches a character.
    for checking in split_string:
        if split_string[check_space] == ' ':
            # To keep checking backwards.
            check_space -= 1
            if count > 0:
                print(count)
                return count
            continue
        count += 1
        check_space -= 1
    return count

def main():
    s = "Hi my name is Brayan"  #<- Change this to your desire input.
    lengthOfLastWord(s)

if __name__ == "__main__":
    main()

