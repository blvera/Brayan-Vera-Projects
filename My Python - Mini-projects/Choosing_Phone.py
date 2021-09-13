#  Program created by Brayan Vera. Date 04/20/2021

#  Program name: "Choosing_Phone"
#  -This program takes user's input who wants to buy a phone
#  depending on what his budget is and what he/she needs.

def choosing_phone():
    user_input = input("Do you prefer iOS or Android? : ")

    if user_input == "Android":
        have_money_q = input("Do you have money? (yes/no): ")
        if have_money_q == "no":
            print("Your phone will be a cheap one under $100.")
        elif have_money_q == "yes":
            camera_matters = input("Is a good camera important for you? (yes/no): ")
            if camera_matters == "no":
                print("Your phone will be an Android around the price of $400.")
            elif camera_matters == "yes":
                print("Your phone will be a Google Pixel Supercamara.")

    elif user_input == "iOS":
        have_money_q = input("Do you have money? (yes/no): ")
        if have_money_q == "no":
            print("Your phone will be a second hand iPhone.")
        elif have_money_q == "yes":
            print("Your phone will be an iPhone Ultra Pro Max")

    else:
        print("Only enter the exact name within the options please, Thank You.")

def main():
    choosing_phone()

if __name__ == "__main__":
    main()