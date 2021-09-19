#  Program created by Brayan Vera. Date 07/21/2021

#  Program name: "Zoo_Discount"
#  -This program tells whether the person who enters the zoo is allowed discount or not.
#  -According to the age and to the identification they have:
#  (Student, Retired, Numerous-Family, Not-applicable)
#  -People that are allowed discount:
#  25 <= age <= 35 and Student (S)
#  age >= 65 and Retired (R)
#  age <= 10
#  card == Numerous-Family (F)

def zoo_discount():
    age = int(input("Tell me your age: "))
    card_type = input("Tell me your kind of identification card \
        (S Student / R Retired / F Numerous-Family / N Not-Applicable): ")

    if (age <= 35 and age >= 25 and card_type == "S") or \
            age <= 10 or \
            (age >= 65 and card_type == "R") or \
            (card_type == "F"):
        print("Zoo discount is applicable.")
    else:
        print("Can't apply zoo discount, sorry.")

def main():
    zoo_discount()

if __name__ == "__main__":
    main()