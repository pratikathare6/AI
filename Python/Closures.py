#Closure -  function "remembers" values from its outer function



def outer():
    x= 10 

    def inner():
        print(x)
    
    return inner


myfunc = outer()
myfunc()