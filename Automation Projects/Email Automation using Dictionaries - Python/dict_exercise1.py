# COUNTING HOW MANY SIMILAR DAYS APPEAR ON THE EMAILS FROM A TEXT FILE

# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan
# 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

#Open file from user
filename = input("Enter a file name: ")

#open the entered file in read mode
fhand = open(filename, 'r')

#create a dictionary called "days"
days = {}

#Getting each line from the user's txt file
for line in fhand:
    #only gets the line that starts with "From " keyword
    if line.startswith("From "):
        #this gets the third word from the line in the txt file
        day = line.split()[2] #PRINTING WITH INDEX 2
        #assigning/adding a key "day" to the dictionary
        #also increments by 1 the value of the key
        days[day] = days.get(day,0) + 1  #if there is no entry for the day in the dictionary (not found) have it as 0

print(days)
