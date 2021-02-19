# DAY 12 OF 100 DAYS OF CODE

#FILE HANDLING

"""
File handling is an important part of any web application.

Python has several functions for creating, reading,
updating, and deleting files.

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
#Open file

f = open("file.txt")

#or

f = open("file.txt","rt") #to open a file , if file is not there it will error

print(f.read(),"\n") #to get the data of file

print(f.read(10),"\n") #specify how many characters you want to return

print(f.readline(),"\n") #You can return one line by using the readline()

f1 = open("file.txt","r")

#By looping through the lines of the file, you can read the whole file, line by line
for x in f1:
    print(x)
print("")


#Close File
"""
It is a good practice to always close the file when you are done with it.

You should always close your files, in some cases, due to buffering,
changes made to a file may not show until you close the file.
"""

f.close()
f1.close()


#Writing to an Existing File
"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
f = open("file.txt","a")
f.write("\nI am writing on this file")
f.close()

f = open("file.txt","r")
print(f.read(),"\n") #reading file
f.close()

f= open("file.txt","w")
f.write("overting current file")
f.close()

f = open("file.txt","r")
print(f.read(),"\n") #reading file
f.close()


#Create new file
"""
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
"""
"""
f = open("newfile.txt","x")
f.close()

f = open("newfile1.txt","a")
f.close()

f = open("newfile2.txt","w")
f.close()
"""

#Deleting File

import os
os.remove("newfile.txt")


#Checking if file exists

if os.path.exists("newfile2.txt"):
    os.remove("newfile2.txt")
else:
    print("File doesn't exists\n")


#Delete Folder
os.rmdir("folder")
