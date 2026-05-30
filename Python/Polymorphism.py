#Polymorphism - may forms - is the ability of a function operator method to behave differently 
# depending on data type or object 
# also called as method overriding
#1. Function polymorphism 

print(len([1,2,3,4])) #here the len function works same on list and string 
print(len('abcdfg'))

#2. Method Polymorphism

class Dog:
    def sound(self):
        print('Dog barks')
    
class Cat:
    def sound(self):
        print('cat meows')
    
d = Dog()
c = Cat()
# in the both classes we have method sound but the working is different 
d.sound()
c.sound()


#3 Operator Polymorphism 

print(5+1)
print('abc'+'def')

# here the operator is + only but works differently on numbers and strings 

