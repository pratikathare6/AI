#When we customize an opeartor for class objects thats called as operator overloading 
#Giving extra meaning to operators for custom objects 

# Without Overloading 

print(5+4)

class Student:
    def __init__(self,marks):
        self.marks = marks 
    #Store the marks in self 

    def __add__(self, other):
        return self.marks + other.marks
    # it tells when we use + then call the __add__ method 
    # when we add the objects the above method is called 

s1 = Student(50)
s2 = Student(60)

print(s1+s2)




