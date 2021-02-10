#3 DAY 100 DAYS OF CODE

#boolean
print(10>1) #true or false value
print("a"=="b")

#bool() to find boolean value
print(bool(1))

#any value is true and non-value is false
print(bool("abv"))
print(bool(""))

#isinstance() to check connection returns true or false
print(isinstance(1,int))

#Operators

#tpes of operators
#Arithmetic operators -> +, -, *, /, %, **, //
print(5+3)
print(5-3)
print(5*3)
print(5%3)
print(5/3) #returns float
print(5**3) #power
print(5//6) # value

#Assignment operators -> =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
x=9
print(x)
x +=3
print(x)#note assignment opearator can't use as arugument
x -=3
print(x)
x *=3
print(x)
x /=3 #returns float
print(x)
x %=3
print(x)
x=9
x //=3
print(x)
x **=3
print(x)
x &=3 #returns same bits
print(x)
x=4
x |=3 #returns one of true bits
print(x)
x=9
x ^=4 #returns one of true bits
print(x)
x >>=3 #returns right shift bits value
print(x)
x <<=3 #returns left shift bits value
print(x)

#Comparison operators -> ==, !=, >, <, >=,<= return boolen value
print(1==3)
print(1!=3)
print(1>3)
print(1<3)
print(1>=3)
print(1<=3)

#Logical operators -> and, or, not return boolean
print(3 and 4) #return second true
print(3 or 4) #return first true
print(not(False)) #return opposite
#Identity operators-> is, is not returns boolean
print(3 is 4)
print(3 is not 4)
#note not to use with litrals although I ahve used it but it's not right way

#Membership operators-> in, not in returns boolean
x=[1,2,3,4]
print(1 in x)
print(5 not in x)

#Bitwise operators-> &, |, ^, ~, <<, >>
print(1&1) #Sets each bit to 1 if both bits are 1
print(1|0) #Sets each bit to 1 if one of two bits is 1
print(1^1) #Sets each bit to 1 if only one of two bits is 1
print(~0) #inverts bits
print(100010001<<1) #Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(100010001>>1) #Shift left by pushing zeros in from the right and let the leftmost bits fall off

