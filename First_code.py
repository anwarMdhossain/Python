'''Python, for example, can be executed as either a compiled program or as an interpreted language in interactive mode. 
So basically, the python program is first compiled and then interpreted. The compilation part is hidden and we believe 
that it is only an interpreted language. The compilation part is done first when we execute our code and this will generate byte code 
and internally this byte code gets converted by the interpreter (python virtual machine). 
And this compiled part gets deleted by the python as soon as you execute your code so that programmers don’t get into complexity.'''

#This is my first program
'''Pyhton is the best general
purpose programming language'''
"""This is another
comment type"""

#The actual syntax of the print() function is:
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#Identity operator (is/is not_ and membership operator (in/not in)

#concurrent program running
import asyncio

async def asyncio_method():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

asyncio.run(asyncio_method())

x=y=5
print(x is y)
print(y is not 6)

#Assert is being used for debugging purpose and it returns AssertionError when condition is False zith the message provided
a=b=6;c=5;
assert a>=5 and c<=6,"Something went wrong in condition"


"""Docstrings appear right after the definition of a function,class, or a module.
This separates docstrings from multiline comments using triple quotes."""

def double(num):
    """This will double the number provided."""
    return num*2
#The docstrings are associated with the object as their __doc__ attribute.
print(double.__doc__)

name=input("Enter your Name: ")
print("Welcome to python tutorial ",name)

print("""How are you
Junaina Parvin""")

print("What are you \ndoing now")

#Reverse a List Using Slicing Operator
systems=['Windows', 'macOS', 'Linux']
print("Original list: ",systems)
reversed_list=systems[::-1]
print("Reversed list: ",reversed_list)

#Accessing Elements in Reversed Order
for st in reversed(systems):
    print(st)

letter=[]
for lt in "human":
    letter.append(lt)
    print(letter)

#Dictionary comprehension
square_dict=dict()
for num in range(1,10):
    square_dict[num]=num*num
    print(square_dict)
    
    
    
