#Program created by Brayan Vera
#Date 09/25/21
# NOW WE WILL SEE HOW TO CAPTURE INFORMATION FROM GROUPS

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls) #the back slashed will print out the second and third group in this case.

#print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match)
    print(match.group(3)) #this depending on the group, it will print only the group in pattern.


# Group zero is everything that we capture. ex. the entire url
