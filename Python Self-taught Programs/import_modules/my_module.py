# Program created by Brayan Vera
# Date: 09/25/21

# In this program we are going to learn how to import modules.
# When we import a module, it runs all of the code that belong to the module.

print("Imported my_module...")

test = 'Test String'

def find_index(to_search, target):
    #Finding the index of a value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
