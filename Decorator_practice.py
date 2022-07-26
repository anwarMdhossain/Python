#Decorator is a function which takes another function as input and returns result without modifying it
#The wrapper function should return the return value of the decorated function, otherwise, it would be lost.

from functools import wraps
def decorator_func(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Before calling decoarted function")
        func(*args,**kwargs)
        print("After calling decorated function")
    return wrapper

@decorator_func
def printMessage(msg):
    '''this is actaul function to be decorated'''
    print("Hello decorated function")
    print("My name is "+msg)

printMessage("Anwar")

print(printMessage.__name__)
help(printMessage)

#You can pass arguments to a decorator by wrapping them inside of another decorator function.
import functools

def repeat_decorator(num_times):
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator_func

@repeat_decorator(num_times=3)
def printMessage(msg):
    '''this is actaul function to be decorated'''
    print("Hello decorated function")

#above statement is equivalent to below ones
#printMessage=repeat_decorator(num_times=3)(printMessage)

printMessage("Anwar")
print(printMessage.__name__)
help(printMessage)

************************************************
def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])

        func()

    # returning inner function
    return inner

@decorator(like="geeksforgeeks")
def my_func():
    print("Inside actual function")

************************************************
def decorator_func(x,y,z):
    print("Inside parameterized decorator function")
    def inner(func):
        print("Inside inner function")
        def wrapper(*args):
            print("Inside wrapper function")
            sum=x+y+z
            print("Summantion of {0},{1} and {2} is {3}".format(x,y,z,sum))
            func(*args)
        return wrapper
    return inner

#@decorator_func(1,2,3)
def print_elements(*args):
    for ele in args:
        print(ele)

decorator_func(1,2,3)(print_elements)("Geeks","for","Geeks")


#Memoization in python to store intermidiate result in case of recursive program

memory={}
def decorate_factorial(func):
    print("Inside decorator function..")
    def wrapper(num):
        if num not in memory:
            memory[num] = func(num)
            print("Result is stored in memory set")
        else:
            print("Result is fetched from memory")
        return memory[num]
    return wrapper

@decorate_factorial
def factorial(num):
    if num == 0:
        result=0
    elif num==1:
        result=1
    else:
        result =num*factorial(num-1)
    return result

print(factorial(5))
print(factorial(6))
print(factorial(6))

**********************************************************
#class as decorator
import functools

class ClassDecorator:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        self.func=func
        self.no_of_calls = 0
    def __call__(self, *args, **kwargs):
        self.no_of_calls +=1
        print(f"{self.no_of_calls} no of calls to {self.func.__name__}")
        return self.func(*args,**kwargs)

@ClassDecorator
def printMessage():
    print("Hello Python!!")

printMessage()
printMessage()
print(printMessage.__name__)


#another example
class Decorator:
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        print("I am inside __call__() method of class")
        result= self.func(*args,**kwargs)
        return result

@Decorator
def printMessage(greet,value,message="Programiz"):
    print("{} {}".format(greet,message))
    return value*2

print("Result is:",printMessage("Hello",5))

