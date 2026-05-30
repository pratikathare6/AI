# Python provides 3 global functions math filter reduce

#1. Map - its a function that accept a function and one argument retrun a seperate list
    # its iterate on each number in a list and return the result 

number = [1,2,3,4,5]

def square(num):
    return num * num 

result = map(square,number)

print(list(result)) #result needs to be converted into list 


#2. Filter - it filters the values based on the condition
 
number2 = [2,3,4,8,9]

def even(num): 
     return num%2==0
        
evenNumbers = filter(even,number2)

print(list(evenNumbers))


#3. Reduce - it combines all the elemnts from the list and returns a single value (need to import)
from functools import reduce

numbers3 = [1,2,3,4]

reduced = reduce(lambda x,y : x+y, numbers3)

print(reduced)

