

#import my_module
#import my_module as mm                       # Changing my_module to mm for short size purpose.
#from my_module import find_index             # allows us to use find_index directly, no need to call my_module every time
from my_module import find_index, test       # having the comma then the variable after allows us to have access to it.
#from my_module import find_index as fi, test # we can still change the variable name with 'as' keyword like this.
#from my_module import *                       # The way to import everything. But we also do not know what came from that module
import sys
import random
import math
import datetime #<---THIS IS VERY USEFUL
import calendar
import os

courses = ['History','Math','Physics','CompSci']

#index = fi(courses,'Math')
index = find_index(courses,'Math')
# print(index)
# print(test)
print(sys.path)
# HOW DOES IT RUN:
#  -1st, it runs the directory that contains the script that we are running.
#  -2nd, the it adds the standard library directories. (allows us to import those
#       modules)
#  -3rd, it adds the site-packages directory for 3rd party packages.

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

#to get today's date
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# To see the path of the directory whe are in, and then perform our work in it.
print(os.getcwd())



'''
HOW DOES IT LOCATE the MODULE:
-The location that it checks is called sys.path
    import sys    then calling parint(sys.path)  <-- to see the path

MODULES HAVE TO BE IN THE SAME DIRECTORY
-Only that way it can be run and compile, otherwise it will fail.

WHEN MODULES NOT IN THE SAME DIRECTORY
-We can manaually make a path to it by appending it. Writing the code below.
-import sys
-sys.path.append('/Users/BrayanVera/Desktop/my-module')

-Can also do it by changing the path in the TERMINAL
- nano ~/.bash_profile
-- (then at the bottom type this below)
- export PYTHONPATH="/Users/BrayanVera/Desktop/my_module"  <---Your module
  location.
  -- (when can check by retarting the terminal and run 'python' (<-type this) the
  'import my_module' (<--your module name)) then type 'sys.path' to see the path.

'''