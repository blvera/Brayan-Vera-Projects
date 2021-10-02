#Program created by: Brayan Vera
#Date: 09/25/21

# The way to aopen a file : with context manager (recommended )
import os

# #When using with open, then you do not need to close it
# with open('test.txt','r') as f:
#     #f_contents = f.read()         # Prints the line of the file.
#     #f_contents = f.readlines()    # This puts the elements of the file in a LIST
#     #f_contents = f.readline()      # This prints only the first line of the file
#     #print(f_contents, end='')      # Having that end='' prevents a new line to be added.
#     #f_contents = f.readline()
#     #print(f_contents, end='')

#     # This prevents load all at once having memory issue
#     # This reads line by line
#     # for line in f:
#     #     print(line,end='')

#     # This gets THE FIRST 100 CHARACTERS
#     # f_contents = f.read(100)
#     # print(f_contents, end='')

#     # This way we PREVENT PRINTING EEMPTY STRINGS when there is no more elements
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)
#     f_contents = f.read(size_to_read)
#     print(f_contents)

#     #print(f.tell())    #Tells you the position of the file
#     # while len(f_contents) > 0:
#     #     print(f_contents, end='')
#     #     f_contents = f.read(size_to_read)

# with open('Test_2.txt', 'w')as f:
#     f.write('Test') #writing to the file
#     f.seek(0)
#     f.write('h')

#WRITING FILE completely FROM READ MODE OF OTHER write File mode
with open('test.txt','r')as rf:
    with open('test_write','w') as wf:
        for line in rf:
            wf.write(line)

#f = open('test.txt','r') #<-- not recommended to open this way IN READ MODE

#COPYING PICTURES USING "FILE OBJECTS" IN PYTHON.
# We have to read and write "bytes" to do this.
with open('puppy.png','rb')as read_file:
    with open('puppy_copy1.png','wb')as write_file:
        # for line in read_file:
        #     write_file.write(line)
        chunk_size = 4096
        rf_chunk = read_file.read(chunk_size)
        while len(rf_chunk) > 0:
            write_file.write(rf_chunk)
            rf_chunk = read_file.read(chunk_size)



'''
OPENING MODES:
 -if you want to read to a file = use 'r'
 -if you want to write to a file = use 'w'
 -if you want to append to a file = use 'a'
 -if you want to read and write to a file = use 'r+'
'''
#still having access to the 'f' file
#print(f.closed)


#Whenever opening the file, you need to explicitely clode is using close()
#f.close()