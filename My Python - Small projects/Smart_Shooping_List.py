#  Program created by Brayan Vera. Date 07/05/2021

#  Program name: Smart_Shooping_List
#  -The program is about a smart shooping list that allows the user to remember
#  the products he/she is willing to shop in the future.
#  -Every time the user wants to add to it's list, a confirmation message appears
#  to avoid spelling errors from the user.
#  -Once the user want to exit the program, the recorded shooping list prints.

def shooping_list():
    print("\nWelcome, let's create your shooping list!")
    list = []
    user_list = None
    user_list = input("\nWhat do you want to buy. Press [Q] to exit: ")
    while user_list != "Q":

        user_list = input("\nWhat else do you want to buy. Press [Q] to quit and view your list: ")
        if user_list == "Q":
            pass
        elif user_list in list:
            print("\n{} is already in the list!\n".format(user_list))
        elif user_list not in list:
            confirmation = input("\nAre you sure you want to add '{}'? [yes or no]: ".format(user_list))
            if confirmation == "yes":
                list.append(user_list)
                print("\n{} added!\n".format(user_list))
            elif confirmation == "no":
                print("")

    print("\nYour shooping list consists of:\n{}".format(list))

def main():
    shooping_list()

if __name__ == "__main__":
    main()