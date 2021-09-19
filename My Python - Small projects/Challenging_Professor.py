#  Program created by Brayan Vera. Date 04/15/2021

#  Program name: "Challenging_Professor"
#  -This program is designed to tell you a story of a student who has the
#  courage to challenge his professor to earn himself some respect.
#  -He thinks that he is in obligation to turn in his exam late
#  because he knows that the professor delivered the exam late.

import random

def challenging_professor():
    first_num = random.randint(30, 90)
    second_num = random.randint(30, 90)

    enter_story = input("""\nWelcome to this story game that proves that a student is smarter than his professor.\n
            Let's get started:\n
            * The story begins when I found myself waiting to take my math final exam.\n
            * My professor had taken his time to deliver the exam 10 minutes after.\n
            * I was mad because we were also told to turn it in at the exact time with no grace time.\n

            # Question 1:
            - Would you like to know more about the story. Type(yes or no): """)

    if enter_story == "yes":
        turn_in_exam = input("""\n
        Let's continue:\n
        * When the exam time finished, the professor asked us to turn in the exam and to put pencils down.\n
        * I saw how everyone in fear to get points deducted would just stand up and give him the exam.\n
        * In the meantime I was thinking on doing either 2 of the following actions.\n
        * Action "A": Continue the exam and take the remaining 10 min that were taken away from me to finish it.\n
        * Action "B": Turn in the exam and feel oppressed just like the others.\n

        # Pregunta 2:
        - What do you think I did. Type "A" or "B": """)

        if turn_in_exam == "B":
            exit("""I did not do that action. End of the Story\n
            Thank you for playing, Bye!""")
        elif turn_in_exam == "A":
            professor_ans = input("""\n
            Yeah that's right:\n
            * I took my 10 minute grace time to continue my exam and earn some respect.\n
            * Then I went to my professor's table and handed it in.\n
            * My professor had 2 answers for me:\n
            * Option "1": You took to much time. I am going to rip off your exam in front of everyone.\n
            * Option "2": Good, I was expecting to see some courage around here. Now answer this.\n
            # Pregunta 3:
            - What do you think my professor said type: 1 or 2: """)
            if professor_ans == "2":
                user_ans = int(input("""\n
                Well yes:\n
                * What is {} * {} and I'll accept your exam.
                = Your answer is : """.format(first_num, second_num)))
                multiplication_ans = first_num * second_num

                if multiplication_ans == user_ans:
                    print("""\n
                    Good Job.\n
                    * I told him, the answer is {} and now we have mutual respect, good bye.
                    GAME OVER""".format(multiplication_ans))
                    
                elif user_ans != multiplication_ans:
                    print("Let's try again. The answer was {}".format(multiplication_ans))
                else:
                    exit("Only numbers are accepted.")
            if professor_ans == "1":
                print("""\n
                Yeah, then:
                * I said, do you know who I am? and he said no.\n
                * Well good, so I put my exam in the middle of the exam pile and left the room.\n
                * This means that he cannot identify who I am and therefore has to accept my ecxam regardless. GAME OVER""")
        else:
            exit("Only enter within the options please. Try the game again. GAME OVER")

    elif enter_story == "no":
        print("It was an awesome story, you missed it. GAME OVER")

    else:
        exit("Only enter within the options please. Try the game again. GAME OVER")


def main():
    challenging_professor()

if __name__ == "__main__":
    main()