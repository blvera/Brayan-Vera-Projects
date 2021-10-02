#Program created by Brayan Vera
#Date 09/25/21

'''
# Topic: "REGULAR EXPRESSIONS":
    - Allows us to search for and match specific patterns of text.
    - Thee is so much we can do with them, so that's why they look complicated
    - We can create a regular expression just for any pattern that we can think of.

# This program is going to search for some specific patterns
# To use REGULAR EXPRESSIONS, we need to "import re" module
'''

import re
from typing import Pattern

# The text that we are going to be searching here is this multiline here under
# the variable text_to_search
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
#Simple sentence that we are going to use in an example
sentence = 'Start a sentence and then bring it to an end'

# WRITING EXPRESSIONS and searching for some patterns.
# We are going to use the RE compile method.
# The compile method will allow us to separate our patterns into a variable
#   and will alow us to make it easy to reuse the variable to perform multiple searches.

#pattern = re.compile(r'abc')  #<----- searching for inside the parenthesis
                                    # the r in the parenthesis makes it a raw string.

#the technique that we implement her is called escaping with the backslash.
#pattern = re.compile(r'\.') #<--- the backslash allows python to look only for the symbol

'''LITERAL SEARCHING'''
#matching an exact url, we need to escape that dot in ti by doing 
#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'[1-5]')            #<- Will print all the numbers found between 1 and 5
#pattern = re.compile(r'[a-zA-Z]')         #<- This will look for all alphabetical letters lowercase and uppercase
#pattern = re.compile(r'[^a-zA-Z]')        #<- This will negate all lower and upper case alpha letters
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')#<- Allow us to specifi the amount of digits that we want to match.
pattern = re.compile(r'Mr\.?')             #<- Will match with or without period after Mr
pattern = re.compile(r'Mr\.?\s[A-Z]\w+')   #<- The + sign means that will read/match 1 or more characters after it
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')   #<- The * sign mean tht it will match 0 or more 
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')   # Creating groups which are the parenthesis

pattern = re.compile(r'start', re.IGNORECASE) # Using FLAGS to accept both lower and upper case

#notice how pattern is label below
matches = pattern.finditer(text_to_search)  #what we want to SEARCH IN put in parenthesis
#the finditer() gathers all of the matches.

#matches = pattern.search(sentence)


'''Performing SEARCHING'''
for match in matches:
   print(match)
#     <re.Match object; span=(1, 4), match='abc'>
#     HOW TO READ:
#     the span=(1, 4) means the beginning (1) and end index (4) of the match
#     it only found 1 match and it found it in the alphabet of indexes 1 to 4

#Printing out the indexes from 1 to 4 in this way
#print(text_to_search[1:4])
 

'''Wanting to match thephone numbers above with a multiline string.'''
#Cannot just type a literal search because they are all different.
# with open('data.txt','r') as data_file:
#     contents = data_file.read()
#     matches = pattern.finditer(contents)
#     #Getting all the phone number matches in this way from data.txt 
#     for match in matches:
#         print(match)

