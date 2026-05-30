#Lamda - lambda function is a small, anonymous function that is defined without a name using 
        # the lambda keyword. Unlike standard functions defined with def, lambdas are restricted 
        # to a single expression and are typically used for short-lived, one-off tasks
        #its like arrow function in javascript 

a = lambda num : num * 2

print(a(21))

c = lambda a,b: a*b
# a,b are the arguments to the lambda and a*b is the operation that we want to perform on that arguments
print(c(20,30))
