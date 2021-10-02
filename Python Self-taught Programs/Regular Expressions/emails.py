#Program created by Brayan Vera
#Date 09/25/21

import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
#Writing a regular expression that will match all those emails.
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
#pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

#THERE ARE A LOT REGULAR EXPRESSIONS FOR EMAILS ONLINE

matches = pattern.finditer(emails)

for match in matches:
    print(match)
