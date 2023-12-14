# File is a named location on disk to store related information.
# It is used to permanently store data in a non-volatile memory (e.g. hard disk).
# When we want to read from or write to a file we need to open it first. 
# When we are done, it needs to be closed, so that resources that are tied with 
# the file are freed. Hence, in Python, a file operation takes place in the 
# following order.
# ● Open a file
# ● Read or write (perform operation)
# ● Close the file

# The open Function
# Before you can read or write a file, you have to open it using Python's built-in 
# open() function.

# Syntax
# file object = open(file_name [, access_mode][, buffering])
# here
# file name -- name of the file you want to access
# access_mode: The access_mode determines the mode in which the file has 
#to be opened, i.e., read, write, append, etc. (by default:read(r))

# Buffering:
# ➔ If the buffering value is set to 0, no buffering takes place. 
# ➔ If the buffering value is 1, line buffering is performed while accessing a file.

# file attributes
# file.closed --> returns true if file is closed.
# file.mode --> returns the access mode with which file was opened.
# file.name --> returns the name of the file.

# open a file
file_obj=open('new.txt','r')
print('name of the file:',file_obj.name)
print('mode of the file:',file_obj.mode)
print('file is closed or not:',file_obj.closed)

print("---------------------------------------------------------------")


# The close() method of a file object flushes any unwritten information and 
# closes the file object, after which no more writing can be done.

file_obj.close()

# write mode(w): opens the file for writing. Overwrites the file if file exists.
# if the file doesn't exists it will create new file for writing.

file_obj2=open('sample.txt','w')
file_obj2.write("Yeah We won the match")
file_obj2.close()

print("------------------------------------------------------------------------------")

# Using 'with' statement to automatically close the file
file_path = 'sample.txt'
with open(file_path, 'r') as file:
    data = file.read()
    print(data)
# # File is automatically closed after this block

# Appending to a File:
# Appending data to an existing file can be done by opening the file in append mode ('a')
# and using the write() method.

# Open a file in append mode and add more data
file_path = 'sample.txt'
with open(file_path, 'a') as file:
    file.write('Appending more data to the file.\n')

# The read() method in Python is used to read the contents of a file.
# It reads the entire file or a specified number of bytes if an argument is provided,
# returning the content as a string

with open('sample.txt', 'r') as file:
    content = file.read()  # Reads the entire content of the file
    print(content)
   
print("---------------------------------------------------------------")

with open('sample.txt','r') as file:
    content2=file.read(4)
    print(content2) 

# The readlines() method in Python is used to read lines from a file and 
# return them as a list of strings. Each string represents a line in the file,
# including the newline character at the end of each line.

with open('file.txt', 'r') as file:
    lines = file.readlines()  # Reads all lines in the file and returns a list
    for line in lines:
        print(line.strip())  # Print each line, removing the newline character
        # print(type(lines))

print("-----------------------------------------------------------------")

# In Python, the tell() method in file handling returns the current position (in bytes) 
# of the file cursor. The file cursor represents the location in the file where 
# the next operation (read or write) will occur.

with open('file2.txt', 'r+') as file:
    content = file.read(20)  # Reads the first 20 bytes
    position = file.tell()   # Retrieves the position after reading
    print(f"Content read: {content}")
    print(f"Current position after reading: {position}")
    
    file.write("\nAppending data")  # Writes additional data
    new_position = file.tell()     # Retrieves the position after writing
    print(f"New position after writing: {new_position}")

# here r+ means opens a file for reading and writing.

# seek() method is used with file objects to change the current position of the file pointer. 
# Opening a file in read mode
file = open("example.txt", "r")

# Move the pointer to the 10th byte from the beginning of the file
file.seek(10)

# Read from the current position
data = file.read()
print(data)

        











