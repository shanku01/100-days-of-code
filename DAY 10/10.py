#DAY 10 OF 100 DAYS OF CODE

#Dates

import datetime
"""
A date in Python is not a data type of its own,
but we can import a module named datetime to work with dates as date objects.
"""

x= datetime.datetime.now()
print(x,"\n")
print(x.year,"\n") #getting year
print(x.strftime("%A"),"\n") #getting day


#Creating Datetime

y = datetime.datetime(2021,2,17)
print(y,"\n")


#strftime()
"""
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(),
and takes one parameter, format, to specify the format of the returned string

%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)
"""
print(x.strftime("%B"),"\n")
print(x.strftime("%a"),"\n")


#Python Math

#Built in math functions

#min() and max()
print(min(2,5,1),"\n")

print(max(2,5,1),"\n")


#abs() to get positive number
print(abs(-5.23),"\n")


#pow() to get power
print(pow(6,2),"\n")


#Math Module

import math

print(math.sqrt(49),"\n") #getting root

print(math.ceil(1.4),"\n") #getting the ceiling number

print(math.floor(1.4),"\n") #getting the floor number

print(math.pi,"\n") #getting the constant pi


#Pyhton JSON

import json

x = '{"name":"shasha","age":23}' #Json string
print(type(x),"\n")
y = json.loads(x) #parsing json stirng to pyhton dictionary

print(y["age"],"\n")

x = {"name":"shasha","age":23}
print(type(x),"\n")

#Dictionary to json 
y = json.dumps(x,indent =4) 

print(y,"\n")

"""
you can cahnge any data type to json using dumps()
"""
print(json.dumps(True),"\n")


#Format Json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x),"\n") #no format

print(json.dumps(x,indent=4),"\n") #indent

print(json.dumps(x,indent=4,separators=("."," = ")),"\n") #using separators

print(json.dumps(x,indent=4,separators=("."," = "),sort_keys=True),"\n") #sorting





