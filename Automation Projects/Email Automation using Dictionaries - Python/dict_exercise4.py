# RECORD THE DOMAIN NAME AND COUNT EXISTANCE INSTEAD OF THE WHOLE EMAIL ADDRESS

# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


#Open file from user
filename = input("Enter a file name: ")

#open the entered file in read mode
fhand = open(filename, 'r')

#create a dictionary called "domain"
domains = {}

#Getting each line from the user's txt file
for line in fhand:
    #only gets the line that starts with "From " keyword
    if line.startswith("From "):
        #this gets the second word from the line in the txt file
        email = line.split()[1]
        #this gets the second element from the email splitted address
        domain = email.split("@")[1]
        domains[domain] = domains.get(domain,0) + 1

print(domains)