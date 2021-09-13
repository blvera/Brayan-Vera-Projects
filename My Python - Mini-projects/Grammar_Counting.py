#  Program created by Brayan Vera. Date 05/15/2021

#  Program name: "Grammar_Counting"
#  -This program counts for spaces, periods, commas and letters that user inputs.
#  Returns the numbers of such elements found in input.

def grammar_count():
    user_text = input("""\nThe machine will count for: spaces, periods, commas and letters.\n
    Now Enter phrase please: """)

    space_counter = 0
    period_counter = 0
    commas_counter = 0
    letter_counter = 0

    for letter in user_text:
        if letter == " ":
            space_counter += 1
        elif letter == ".":
            period_counter += 1
        elif letter == ",":
            commas_counter += 1
        elif letter.isalpha():
            letter_counter += 1

    print("Spaces = {}\n"
        "Periods = {}\n"
        "Commas = {}\n"
        "Letters = {}\n".format(space_counter,period_counter,commas_counter,letter_counter))

def main():
    grammar_count()

if __name__ == "__main__":
    main()
