# Program created by Brayan Vera
# Date 09/12/21

# Learning about variable scope in python.
'''
L E G B: Local, Enclosing, Global, Built-in
'''
# Helps when a variable may not have a variable that we expected and we need to
# debug our code.
# Variable scope: serves us to understand where variables can be accessed from
# within the program and what those variables hold within the context

# Local:     variables defined within a function.
# Enclosing: variables in the local scope of the enclosing functions.
            #has to do with nested functions.
# Global:    variables defined at the top level of a module or explicitely
           # declaring global using the 'global' keyword.
# Built-in:  names that are pre-assign in python such as sorted(), min(), etc
            #builtin functions cannot be overwritten,

# Reason the abreviation LEGB is in this order is because this is the order that
# determines what order is being assigned to. Checks variables from L first to B
# last.
#----------------------------------------
# x = 'global x' #Global variable

# def test(z): #this z is only going to exist within the function, not outside
#     #global x  #setting global x explicitely here inside the func
#     x = 'local x'
#         #y = 'local y' #Local variable to this test function.
#         #print(y) # y is printed from local scope
#         #print(x) #This prints x because x is defined global.
#     print(x) #This x is printed from the local x defined in the func, the global x does not overwrite it


# test() #Looks in the local scope first.
# #print(y) #Throws an error bc 'y' does not live outside the function
# ## print(x) # Looks in the Local -> Enclosing -> Global (found in the global)
# print(x)
#-----------------------------------------

# ENCLOSING PART

# def outer():
#     x = 'outer x'

#     def inner():
#         #x = 'inner x'
#         print(x) #Looks for LOCAL -> ENCLOSING(found) prints the x in outer()
#     inner()
#     print(x) #prints the x in the outer()

# outer()
# #print(x)

# Using 'nonlocal' in this exercise
# def outer():
#     x = 'outer x'
#     def inner():
#         #nonlocal is mainly use to change the state for closures and decorators
#         nonlocal x #This makes the x above to be overwritten with the x below
#         x = 'inner x'
#         print(x)

#     inner()
#     print(x)

# outer()

x= 'global x'
def outer():
    #x = 'outer x'
    def inner():
        #x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)









