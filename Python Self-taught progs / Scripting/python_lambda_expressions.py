#  Program created by Brayan Vera. Date 09/14/21

#  Program name: python_lambda_expressions
#  They are known has anonymous function (or lambda expressions) bc it does not have a name.
#  -lambda expressions are so useful when you need a short throw away functions, somethign simple that you will only use once.
#  common aplications fro lambda are sorting and filtering data.

def compute_equation(x):
    print(3*x+1)
    return 3*x +1

def build_quadradic_functions(a,b,c):
    return lambda x: a*x**2 + b*x + c

def main():
    x = 2
    # The usual way.
    # Writing a function to compute 3x+1.
    compute_equation(x)

    # Example 1
    # Creating a "LAMBDA EXPRESSION":
    # This anonymous function will enter the input x and return the output 3*x+1.
    # As of now, we cannot use it, so we declare it to a variable.
    #lambda x: 3*x + 2
    g = lambda x: 3*x + 1  #<--- declaring it to a variable.
    print(g(4)) #<---- we cannot use the x value that is declared above. We provide a value to the function.

    # Example 2
    # LAMBDA EXPRESSION WITH MULTIPLE INPUTS.
    # Combining first name and last name into a single "Full Name"
    # -removing the leading and trailing whitespace with .strip()
    # -only the first letter of each string(name) has to be capatilized with .title()
    full_name = lambda f_name, l_name: f_name.strip().title() + " " + l_name.strip().title()
    print(full_name("rubious    ", "aURON"))

    # Example 3
    # Suppose we have a list of science fiction authors and we want to sort this list by last names.
    # We notice that some of these authors have a middle name and others have initials
    # Our strategy will be to create an anonymous function that extracts the last name and uses that
    #  to sort the list.
    scifi_authors = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthurs C. Clarke", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
    # help(scifi_authors.sort)
    # sort(*, key=None, reverse=False)
    # To access the last name using lamba, split the strings into pieces werever it has a space
    #  and then access the last piece by index [-1] and convert the string to lower case .lower()
    #  converting it to lower makes sure the sorting is not case sensitive.
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower(), reverse=False)
    # Now the list with sci fiction authors will be sorted by scending order
    print(scifi_authors)

    # Example 4
    # Now writing a function that makes functions
    # Suppose we are working with quadratic functions , exampple, computing the tragectory of a cannon ball
    # Should return the function f(x) = ax^2 + bx + c 
    f = build_quadradic_functions(2,3,-5)
    print(f(0)) #prints -5
    print(f(1)) #prints 0
    print(f(2)) #prints 2

    # Example 5
    # Using a quadratic functino without ever giving it a name
    h = build_quadradic_functions(3,0,1)(2)  # 3x^2+0x+1 evaluated for x=2 --> should output 13
    print(h)

if __name__ == "__main__":
    main()