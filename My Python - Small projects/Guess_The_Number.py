#  Program created by Brayan Vera. Date 06/10/2021

#  Program name: "Guess_The_Number"
#  -This simple program asks the user what number the computer is thinking about.
#  -If entered number is correct, a celebration message is printed.
#  -If entered number is incorrect, then GAME OVER.
#  -The Program does not accept invalid inputs such as other number that is not in-
#  the range of 1 and 10 or other inputs that are not numbers.

import random

def guess_number():
    print("\nWelcome to the game 'guess the number and win'\n")

    user_num = int(input("Enter the number that you think the computer is thinking about: "))
    computer_num = random.randint(1,10)

    if user_num > 10 or user_num < 1:
        print("""\nEnter a number only within the range of 1 and 10 please.\nPlay game again.""")
    elif user_num == computer_num:
        print("\nCongrats, you are a witch, you guessed the computer number!!!")
    elif user_num != computer_num:
        print("\nGame Over, the computer number is {}".format(computer_num))


def main():
    guess_number()

if __name__ == "__main__":
    main()