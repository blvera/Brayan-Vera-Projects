import os
# Fernet is autenticated cryptography that won't allow us to read/modify the
# file without having a key. So we have to create a key.
from cryptography.fernet import Fernet
# Getting into the directory where I have the file stored
os.chdir('/Users/BrayanVera/Desktop/Automation_Projects/encrypting_file')

# # Creating a key. This is stored in the local memory.
# key = Fernet.generate_key()

# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)  #going to be using this to encrypt and decrypt code

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)

Generating encrypted files.
#initialize our ferenet object and initialize our key there
f = Fernet(key)

# Reading the original text and storing it as original
with open('RawAlert_plain_result.txt', 'rb') as original_file:
    original = original_file.read()

# Encrypting the data using the fernet object as our key and storing it as
# encrypted.
encrypted = f.encrypt(original)

#writing it into a new .csv file
with open('encrypted_text.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# #decrypting it back to original content
# f = Fernet(key)

# #read our encrypted data and save it as encrypted
# with open('Encoded_raw_alert.txt', 'rb') as encrypted_file:
#     encrypted = encrypted_file.read()

# # Now decrypting the data using the Fernet object with our key and will saved it
# # as decrypted
# decrypted = f.decrypt(encrypted)

# with open('decrypted_file.txt', 'wb') as decrypted_file:
#     decrypted_file.write(decrypted)

'''
My Approach:
-I am encrypting the 'RawAlert_plain_result.csv' file into a new file name
-Then I am decrypting the encrypted file and I get the result.
'''
