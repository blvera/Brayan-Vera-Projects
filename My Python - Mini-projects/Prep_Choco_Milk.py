#  Program created by Brayan Vera. Date 06/23/2021

#  Program name: "Prep_Choco_Milk"
#  -This program interacts with the user to prepare some chocolate milk.
#  -The program also advices user to buy the missing product before the preparation.

def prepare_chocolate_milk():
    print("\nToday we Will prepare chocolate milk. Let's go to the kitchen.")
    print("\nOpening the fridge.")

    milk_found = input("\nIs there milk? (yes or no): ")
    chocolate_found = input("\nIs there chocolate powder 'Nesquik'(yes or no): ")

    if milk_found == "yes":
        if chocolate_found == "yes":
            print("\nGreat, now we are ready to begin.\n")
            print("* 1st: We pour some milk in an empty glass.")
            print("* 2nd: We put some Nesquik powder on the same glass")
            print("* 3rd: We grab a spoon and stir it")
            print("\nWe are done, enjoy your drink!")
        elif chocolate_found == "no":
            print("\nLet's go buy some Nesquik.")

    if milk_found == "no":
        if chocolate_found == "no":
            print("\nLet's go buy Nesquik and milk")
        elif chocolate_found == "yes":
            print("\nLet's go buy only milk.")

def main():
    prepare_chocolate_milk()
    
if __name__ == "__main__":
    main()





