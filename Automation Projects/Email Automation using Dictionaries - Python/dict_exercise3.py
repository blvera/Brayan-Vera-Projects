# COUNTING WHO HAS THE MOST EMAILS AND THEIR REPEATED NUMBER

# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section [maximumloop]) to find who
# has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

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

max_addrs = None
max_emails = 0
for i in email_addrs:
    #checking the value of the current key
    if email_addrs[i] > max_emails:
        max_addrs = i  #this gets the key | to get the max key(email address) name
        max_emails = email_addrs[i] #for the current value | to get the max value number

print(max_addrs, max_emails)
