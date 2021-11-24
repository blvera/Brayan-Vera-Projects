
#Dictionary:
# First goes the key, the the values.
student = {'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

#adding to the end of the dictionary
student['phone'] = '555-5555'  #This gets added to the end of the dictionary

#updating keys in the dictionary
student['name'] = 'Jane'

#updating keys in just one statement: name, age and adding a key
student.update({'name':'Robert', 'age':27, 'phone': '788-8888'})

#delete specific key or value
#del student['age']

#deleting and storing the value
#age = student.pop('age')

#to see if our dictionary key length (will return the amount of keys)
#print(len(student))

#To check all the keys only
#print(student.keys())

#To get all the values only
#print(student.values())

#To see the keys and values
#print(student.items())

#To loop through keys and values
for key, value in student.items():
    print(key,value)


#print(student) #prints the entire dictionary
#print(student.get('phone', 'Not Found'))  #returns "None"  or other thing by default for keys that do not exist
#print(age)
