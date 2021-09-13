#  Program created by Brayan Vera. Date 07/25/2021

#  Program name: "Currency_Converter"
#  -This program converts dollar, euro and pound to each other.
#  -If the user makes a mistakes and not chooses within the options,
#  then the program quits and kindly asks the user to run the program again.

dollar_to_euro = 0.91
euro_to_dollar = 1.21
pound_to_euro = 1.18
euro_to_pound = 0.87

def currency_converter():
    user_option = input("""Welcome to the currency convertor.\n
            Option A: From Dollar to Euro
            Option B: From Euro to Dollar
            Option C: From Pounds to Euro
            Option D: From Euro to Pounds
            \nWhat currency would you like to convert today, you have 4 options above: """)

    if user_option == "A":
        dollar_input = float(input("Input the dollar amount: "))
        the_change = dollar_input * dollar_to_euro
        input("""\nYour change from Dollar to Euro is: {}\n
            \nThanks for using the currency converter. Have a great day!""".format(the_change))

    elif user_option == "B":
        euro_input = float(input("Ingresar el monto de euro: "))
        the_change = euro_input * euro_to_dollar
        input("""\nYour change from Euro to Dollar is: {}\n
            \nThanks for using the currency converter. Have a great day!""".format(the_change))

    elif user_option == "C":
        libra_input = float(input("Ingresar el monto de libra: "))
        the_change = libra_input * pound_to_euro
        input("""\nYour change from Pounds to Euro is: {}\n
            \nThanks for using the currency converter. Have a great day!""".format(the_change))

    elif user_option == "D":
        euro_input = float(input("Ingresar el monto de euro: "))
        the_change = euro_input * euro_to_pound
        input("""\nYour change from Euro to Pounds is: {}\n
            \nThanks for using the currency converter. Have a great day!""".format(the_change))

    else:
        print("You entered an incorrect input. Please run program again.")

def main():
    currency_converter()

if __name__ == "__main__":
    main()