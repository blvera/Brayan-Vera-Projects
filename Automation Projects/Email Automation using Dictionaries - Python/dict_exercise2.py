#COUNTING HOW MANY EMAILS EACH EMAIL ADDRESS HAS.

# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}


#Open file from user
filename = input("Enter a file name: ")

#open the entered file in read mode
fhand = open(filename, 'r')

#create a dictionary called "days"
email_addrs = {}

#Getting each line from the user's txt file
for line in fhand:
    #only gets the line that starts with "From " keyword
    if line.startswith("From "):
        #this gets the third word from the line in the txt file
        email = line.split()[1] #PRINTING WITH INDEX 2
        #assigning/adding a key "day" to the dictionary
        #also increments by 1 the value of the key
        email_addrs[email] = email_addrs.get(email,0) + 1  #if there is no entry for the day in the dictionary (not found) have it as 0

print(email_addrs)