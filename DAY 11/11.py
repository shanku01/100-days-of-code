# DAY 11 OF 100 DAYS OF CODE

#RegEx
"""
A RegEx, or Regular Expression,
is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.
"""

import re #built in package

str1 = "I am having good time here"
"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""
print(re.search("here",str1),"\n")

print(re.findall("a",str1),"\n")

print(re.split(" ",str1),"\n")

print(re.sub("here","there",str1),"\n")


#Matacharacters
"""
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group
"""


#Special Sequence
"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"

\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
r"\bain" r"ain\b"

\B	Returns a match where the specified characters are present, but NOT at the beginning
(or at the end)of a word (the "r" in the beginning is making sure that the string is being treated
as a "raw string") r"\Bain" r"ain\B"

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"

\D	Returns a match where the string DOES NOT contain digits	"\D"

\s	Returns a match where the string contains a white space character	"\s"

\S	Returns a match where the string DOES NOT contain a white space character	"\S"

\w	Returns a match where the string contains any word characters (characters from a to Z,
digits from 0-9, and the underscore _ character)	"\w"

\W	Returns a match where the string DOES NOT contain any word characters	"\W"

\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""


#Sets
"""
[arn]	Returns a match where one of the specified characters (a, r, or n) are present

[a-n]	Returns a match for any lower case character, alphabetically between a and n

[^arn]	Returns a match for any character EXCEPT a, r, and n

[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present

[0-9]	Returns a match for any digit between 0 and 9

[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59

[a-zA-Z]	Returns a match for any character alphabetically between a and z,
lower case OR upper case

[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means:
return a match for any + character in the string
"""

#Match Object
"""
A Match Object is an object containing information about the search and the result.
"""

x =re.search("here",str1) #match object
print(x,"\n")

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
print(x.span(),"\n")

print(x.string,"\n")

print(x.group(),"\n")


#PIP
"""
PIP is a package manager for Python packages, or modules if you like.

A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.
cmd - pip install packageName
"""

import camelcase #package I have installed using pip

c = camelcase.CamelCase()

text1 =  "what up!"
text2 = c.hump(text1)
print(text1,text2,"\n")

"""
For uninstalling
cmd - pip uninstall packageName

For listing
cmd - pip list
"""


#Python Try...Except
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

#Exception Handling
"""
When an error occurs, or exception as we call it,
Python will normally stop and generate an error message.

These exceptions can be handled using the try statement
"""
try:
    print(z,"\n")
except NameError:
    print("z not defind","\n")
except:
    print("Something terrible happend","\n")
else:
    print("Nothing went wrong","\n")
"""
You can use the else keyword to define a block of code to be executed if no errors were raised
"""

"""
The finally block, if specified,
will be executed regardless if the try block raises an error or not.
"""

try:
    print(t)
except:
    print("Somthing went bad")
finally:
    print("We will fix it","\n")


#Raise Exception
"""
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
"""
"""
x= -1
if x<0:
    raise Exception("Sorry,no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""


#User Input
"""
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.
"""

name=input("Enter Name: ")
print("Name :",name,"\n")

"""
lName=raw_input("Enter Last Name: ")
print("Last Name :",lName,"\n")
"""


#String Formatting
price = 30
txt = "the price is {} Rupee"
print(txt.format(price),"\n")

"""
You can add parameters inside the curly brackets to specify how to convert the value
"""
txt = "the price is {:.2f} Rupee"
print(txt.format(price),"\n")

"""
If you want to use more values, just add more values to the format() method
"""

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} Rupee."
print(myorder.format(quantity, itemno, price),"\n")

"""
You can use index numbers (a number inside the curly brackets {0})
to be sure the values are placed in the correct placeholders
"""

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name),"\n")

"""
You can also use named indexes by entering a name inside the curly brackets {carname},
but then you must use names when you pass the parameter values txt.format(carname = "Ford")
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Suzuki", model = "Alto"))
