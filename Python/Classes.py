# Classes - class is a blueprint to create objects
# objects - objects are the instance of a class

class animal:
    def walk(self): #method
        print('walking...')



class dog(animal): #inheritance
    def __init__(self,name,age): #constructor
       self.name = name 
       self.age = age
    
    def bark(self): #method
        print('woof')
    

roger = dog("roger",8)

print(roger.name)
print(roger.age)
roger.bark()

roger.walk()