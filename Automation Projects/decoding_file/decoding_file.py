import os

# To be in the same directory where I am working with
os.chdir('/Users/BrayanVera/Desktop/Automation_Projects/decoding_file') #This directory will change based where the file is stored in.

# To open the file (Encoded_raw_alert.txt)in read mode and get the content inside of it.
f = open("Encoded_raw_alert.txt", "r")

# Creating an empty string to pass all the content of the Encoded_raw_alert.txt file
string = ""
for val1 in f:
    string = string + val1

# To make sure the content was passed to the created string.
print("PASSING THE FILE CONTENT TO A STRING:")
print(string)

print ("THE ENCODED STRING IS: ")
print (string)

# This prints the decoded file.
# I have checked what it prints and is the same content as the
# RawAlert_plain_result.txt file
# So this means that my program works successfully. YAY!
print ("THE DECODED STRING IS: ")
print (string.decode('base64','strict'))

# Making a new .txt file with our decoded result in it.
# Naming it 'decoding_file_result.txt'
with open('decoding_file_result.txt', 'wb') as decoding_file:
    decoding_file.write(string.decode('base64','strict'))

# And we are done. Thank You for your time.
