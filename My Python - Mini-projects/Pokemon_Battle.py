#  Program created by Brayan Vera. Date 06/15/2021

#  Program name: "Pokemon_Battle"
#  -This program is a mini pokemon battle game, it let's the user actively
#  have a battle with pikachu.
#  -According to the user's performance, the user can win or lose the battle
#  and is also kindly asked to play again.

import random
import os

# Features added:
# - Making sure the life does not go negative numbers.
# - Clearing the screen every time user presses enter. (In progress)
# - The extra option to not do anything.
def pokemon_battle():
    #Declaring Pikachu moves.
    pikachu_life = 80
    quick_attack = 10
    thunder_shock = 11

    #Declaring Squirtle moves.
    squirtle_life = 90
    tail_whip = 10
    hydro_pump = 12
    tackle = 9

    start_game = None


    while start_game != "X":
        start_game = input("Let's begin this pokemon battle, ma boi! "
                        "Press X to start the game: ")


    print("\nTthis pokemon battle will be Pikachu vs Squirtle\n"
        "The computer will be 'Pikachu' and you will be 'Squirtle'\n"
        "Let the battle begin.......\n")

    print("Pikachu starts with 80% of life\n"
        "PIKACHU life ({}%)->{}\n"
        "Squirtle starts with 90% of life\n"
        "SQUIRTLE life({}%)->{}\n".format(pikachu_life,"#"*pikachu_life, squirtle_life,"#"*squirtle_life))


    while pikachu_life > 0 and squirtle_life > 0:
        if pikachu_life > 0:
            pikachu_attack = random.randint(quick_attack, thunder_shock)

            squirtle_life = squirtle_life - pikachu_attack
            if pikachu_attack == quick_attack:
                if squirtle_life < 0:
                    squirtle_life = squirtle_life * 0
                print("Pikachu attacks with 'Quick Attack' which deduces Squirtle {}% of life.\n"
                    "SQUIRTLE life ({}%) ->{}".format(pikachu_attack, squirtle_life,"#"*squirtle_life))
            elif pikachu_attack == thunder_shock:
                if squirtle_life < 0:
                    squirtle_life = squirtle_life * 0
                print("Pikachu attacks with 'Thunder Shock' which deduces Squirtle {}% of life.\n"
                    "SQUIRTLE life ({}%) ->{}".format(pikachu_attack, squirtle_life,"#"*squirtle_life))

            input("\nPress ENTER to continue!")
            #os.system("clear")

        if squirtle_life > 0:

            user_turn = input("\nYour turn, you have 3 attack options:\n"
                                "A - Tail Whip\n"
                                "B - Hydro Pump\n"
                                "C - tackle\n"
                                "D - Nothing\n"
                                "Your option is: ")
            while user_turn not in ["A","B","C","D"] :
                print("You can only choose within the options of A, B, C or D")
                user_turn = input("\nYour turn, you have 3 attack options:\n"
                                    "A - Tail Whip\n"
                                    "B - Hydro Pump\n"
                                    "C - Tackle\n"
                                    "D - Nothing\n"
                                    "Your option is: ")
            if user_turn == "A":
                print("\nYou are attacking with 'Tail Whip' which deduces Pikachu {}% of life.".format(tail_whip))
                pikachu_life = pikachu_life - tail_whip
                if pikachu_life < 0:
                    pikachu_life = pikachu_life * 0
                print("\nPikachu now has remaining {}% of life.\n"
                    "PIKACHU life ({}%) ->{}\n".format(pikachu_life, pikachu_life,"#"*pikachu_life))
            elif user_turn == "B":
                print("\nYou are attacking with Hydro Pump which deduces Pikachu {}% of life.".format(hydro_pump))
                pikachu_life = pikachu_life - hydro_pump
                if pikachu_life < 0:
                    pikachu_life = pikachu_life * 0
                print("\nPikachu now has remaining {}% of life.\n"
                    "PIKACHU life ({}%) ->{}\n".format(pikachu_life, pikachu_life,"#"*pikachu_life))
            elif user_turn == "C":
                print("\nYou are attacking with tackle which deduces Pikachu {}% of life.".format(tackle))
                pikachu_life = pikachu_life - tackle
                if pikachu_life < 0:
                    pikachu_life = pikachu_life * 0
                print("\nPikachu now has remaining {}% of life.\n"
                    "PIKACHU life ({}%) ->{}\n".format(pikachu_life, pikachu_life,"#"*pikachu_life))
            else:
                print("You skipped a turn. Now is Pikachu's turn\n"
                    "PIKACHU life ({}%) ->{}\n".format(pikachu_life, pikachu_life,"#"*pikachu_life))

    if squirtle_life < pikachu_life:
        print("Pikachu WINS. Try again, pikachu is always ready, GOOD LUCK!")

    elif pikachu_life < squirtle_life:
        print("Squirtle WINS. Congrats, you did it. You are good at this!")


def main():
    pokemon_battle()

if __name__ == "__main__":
    main()
