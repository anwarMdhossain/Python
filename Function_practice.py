#Function in python

#example of pass keyword to not throw any error without having any function body
def printHello():
    pass

def generator():
    for i in range(10):
        yield i*i
g=generator()
#print(g)
for j in g:
    print(j)
    
#global/nonlocal example programme
def outer_function():
    b=10
    global a
    a = 20

    def inner_function():
        nonlocal b
        global a
        a = 30
        b = 15
        print("Here")
        print('a :=', a)
        print('b :=', b)

    print("Here first")
    inner_function()
    print('a =', a)
    print('b =', b)

a = 10
outer_function()
print('a =', a)

#Any number of arguments in a function can have a default value.
#But once we have a default argument, all the arguments to its right must also have default values.
#we can mix positional arguments with keyword arguments during a function call.
#But we must keep in mind that keyword arguments must follow positional argument

def default_arguements(name, msg="Welcome to Python tutorial"):
    print("Hello,"+name+"!!"+msg)

default_arguements("Anwar",)
default_arguements("Anwar","How are you doing?")

#Python Arbitrary Arguments in function parameter

def func_arbit(*args):
    '''This is arbitrary length function.'''
    for ar in args:
        print("Hello "+ar)
        
print(func_arbit.__doc__)
func_arbit("Aaban","Arhab","Rose","Deep")


#Recursive function should have a base condition else it will go on infinitely
#Maximum limit of recurion is 1000 and after that it throws RecursionError

def fact(n):
    if n==0:
        return 1 
    else:
        return(n*fact(n-1))

x =int(input("Enter the number to find factorial: "))
if x>0:
    result= fact(x)
    print("Factorial of {} is: {}".format(x,result))
else:
    print("Input number is not valid!!!")


#Syntax of Lambda Function in python
#lambda arguments: expression
   
#Lambda functions can have any number of arguments but only one expression.
    
double=lambda x: x**2
print("Value is",double(5))

##Filter() function takes two arguement , 1.Function 2. list and return a value in sequence
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
my_tuple=(2,3,4,5,6,7,8,9,10)
new_list=list(filter((lambda x: x%2==0),my_list))
print("New list is",new_list)
new_tuple=tuple(filter((lambda y: y%2==0),my_tuple))
print("New tuple is",new_tuple)

#Map() function takes two arguement and operates on each item of iterable object
new_list=list(map(lambda x:x*3,my_list))
print("New list is",new_list)
new_tuple=tuple(map((lambda y: y*4),my_tuple))
print("New tuple is",new_tuple)

fruits=["Apple","Banana","Lichi","Mango"]
fruits.sort(key=lambda x:len(x))
print("Sorted list",fruits)

#example of global variable in nested function
def foo():
    x=20
    print(id(x))
    print("inside foo function",x)
    def bar():
        global x
        x=25
        print(id(x))
        print("inside bar function",x)
    print("Before calling bar function", x)
    bar()
    print(id(x))
    print("After calling bar function",x)
    
foo()
print(id(x))
print("Ouside of foo function",x)
