## Day 36 of 100 days of code

#Random Algorithm

#Function to check prime
def checkPrime(num):
    
    if num == 1 :
        return True

    elif num == 0:
        return False
    else:
        for x in range(2,num):
            if num%x ==0:
                return False
    return True

#Function to check prime in a range
def countPrime(a,b):
    count=0
    
    for x in range(a,b+1):
        #check every number and updating count
        if(checkPrime(x)):
            count+=1
            
    return count

#Largest number in array
def largest(array):
    largest = 0
    
    for x in array:
        if x>largest:
            largest = x
            
    return largest

#Reverse String
def reverseString(string):
    result =""
    
    for x in string:
        result= x+result
        
    return result

    
#Testing 
print(countPrime(1,11))

print(largest([4,1,8,2,10]))

print(reverseString('hello'))
        
                
