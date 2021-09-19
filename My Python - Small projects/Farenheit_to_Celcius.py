#  Program created by Brayan Vera. Date 05/05/2021

#  Program name: "Farenheit_to_Celcius"
#  -This program converts Frenheit temperature  to Celius according to user's input.
#  -Example: 45F --> 7C and the formula is (x-32)*5/9 = y, where "x" is the initial Farenheit
#  and "y" is the converted temperature in Celcius.

def farenheit_to_celcius():
    start_farenheit = int(input("Introduce the Farenheit degree you wish to convert into Celcius: "))
    conversion = (start_farenheit - 32) * 5/9
    print("The Celsius conversion is: {}".format(conversion))

def main():
    farenheit_to_celcius()

if __name__ == "__main__":
    main()