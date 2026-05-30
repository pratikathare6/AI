# recursion means a function calls itself 

def factorial(n):
    if n==1: return 1
    return n * factorial(n-1)

print(factorial(3))

# decorators - when we want to change the execution sequence of the function we use decorators @

def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@logtime
def hello():
    print('hello')

hello()

#docstring
def print():


    """
    this is the docstring used to document the code

    """

#annotation - : are used to specify the type of a variable 

c:  int = 1 # this is the annotation 

#exceptions - used to catch the errors

try:
    result = 2 / 0
except ZeroDivisionError:
   raise Exception('cannot divide by 0')
finally:
    result = 1
