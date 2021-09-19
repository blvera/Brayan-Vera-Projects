#  Program created by Brayan Vera. Date 05/06/2021

#  Program name: "Found_Uppercase"
#  -The program looks for upper case letters in the user's input and
#  returns how many letters were found.

import string

def found_upper_case():
    user_text = input("Enter text: ")
    uppercase_letters = 0

    for letter in user_text:
        if letter in string.ascii_uppercase:
            uppercase_letters += 1
    print("The uppercase letters found are: {}".format(uppercase_letters))

def main():
    found_upper_case()

if __name__ == "__main__":
    main()