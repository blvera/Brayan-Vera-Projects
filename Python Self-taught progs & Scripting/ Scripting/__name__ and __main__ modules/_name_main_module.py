# Program created by Brayan Vera
# Date 09/24/21

# This program explains the use of __name__ and __main__ and other

#print("First Module's Name: {}".format(__name__)) #the output for this is __main__
# When python runs a file, before even runs any code, it sets a few special variables.
# __name__ is one of those special variables. And when python runs a python file
#directly, it sets this __name__ variable to __main__
#
# We can also import modules, whenever we import a module, is going to set
# __name__  --> to the name of the python file

print("Outside the main") #This gets run anyways since is outside and free.

def main():
    print("First Module's Name: {}".format(__name__))
    print("hello")

if __name__ == "__main__": # Checks if this file runs directly by python or is
                           # it being imported?
    main()
    print("Run Directly")
else:
    print("Run from Import")


# REASON: __name__ and __main__ is used is:
# -Sometimes there is code that you only want to run whenever you are running
# this as the main file.
# -Sometimes there is code that you only want to run whenever if being imported.