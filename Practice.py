#practice
#to print Exception class tree
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)

#yield is similar as return being only difference as it returns a generator
#which generates one value at a time based on requirement
#The difference is that while a return statement terminates a function entirely, 
#yield statement pauses the function saving all its states and later continues from there on successive calls.
g=(2**x for x in range(10))
print(next(g))
print(next(g))

#using generator function
def generate_fibonacci():
    n1=0
    n2=1
    while True:
        yield n1
        n1,n2=n2,n1+n2

fib=generate_fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

#Reverse of string using generator
def rev_str(msg):
    length=len(msg)
    for rev in range(length-1,-1,-1):
        yield msg[rev]

for i in rev_str("Hello"):
    print(i)

#generator expression can be sent as arguement inside function
list1=[1,2,3,4,5]
sum(x**2 for x in list1)

#Example programme to exceute statement asynchronously
import asyncio

async def printHello():
    print('Hello Brother')
    await asyncio.sleep(1)
    print('Hello Sister')

asyncio.run(printHello())


import decimal
print(0.1)
print(decimal.Decimal(0.6))

import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(2,3))
print(fractions.Fraction('1.2'))

#Example of sorted list using key
def takeSecond(el):
    return el[1]

list1=[(1,2),(3,4),(2,3),(4,0)]
list1.sort(key=takeSecond,reverse=False)
print('Sorted list is: ',list1)

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list1=copy.copy(old_list)
new_list2=copy.deepcopy(old_list)
old_list.append([4,4,4,])

#Value should be different
print('Old List: ',old_list)
print('New_list1: ',new_list1)
print('New_list2: ',new_list2)

old_list[0][1]=3

#Elements of nested list should be changed for new_list1 but not for new_list2
print('Old List: ',old_list)
print('New_list1: ',new_list1)
print('New_list2: ',new_list2)

list2=['p','r','o','b','l','e','m']
list2.sort(reverse=True)
print('Sorted list2: ',list2)
print(sorted(list2,reverse=False))

#List comprehension is an elegant and concise way to create a new list from an existing list in Python.
h_letter=[letter for letter in 'human' if letter in ('h','a','n')]
print(h_letter)

#if..else condition
num_list=['even' if x%2==0 else "odd" for x in range(20)]
print(num_list)

# using triple quotes
print('''He said, "What's there?"''')
# escaping single quotes
print('He said, "What\'s there?"')
# escaping double quotes
print("He said, \"What's there?\"")

#Example of enumerate function
str="Hello"
str_enum=list(enumerate(str))
print(str_enum)

# Python string format() method
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

#String methods are format()/lower()/upper()/join()/split()/find()/replace()
print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))
print("{:*^5}".format("cat"))

#SET practice(set is unordered and cannot hold duplicate and mutable elements)
#The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. 
#On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).
my_set=set()
my_set.add(2)
my_set.update([1,2,3],"Hello",{4.5,5.5},(10,20,30))
print(my_set)
my_set.discard(2)
print(my_set)
my_set.remove(5.5)
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

#The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.It can be used as key of dictionary unlike sets
my_set = frozenset((3,4,5,6))
print(my_set)

#When you use a dictionary as an iterable for a frozen set, it only takes keys of the dictionary to create the set.
person = {"name": "John", "age": 23, "sex": "male"}
keys=frozenset(person)
print('Keys are: ',keys)


#DICTIONARY
my_dic=dict([(1,'Anwar'),(2,'Hossain')])
print(my_dic)
my_dict=dict({'name':'Anwar','place':'Durgapur','age':31})
print(my_dict['age'])
#return None
print(my_dict.get('salary'))
my_dict['name']='Anwar Hossain'
print(my_dict)
my_dict['place']='Farakka'
my_dict['profession']='Engineer'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print(my_dict.popitem())
my_dict.clear()

#Dictionary comprehension
squares={x:x*x for x in range(6) if x%2==0}
print(squares)

squares=dict()
for x in range(6):
    squares[x]=x*x
print(squares)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price={item:price*dollar_to_pound for (item,price) in old_price.items() if price*dollar_to_pound>=1}
print(new_price)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict={item:value for (item,value) in original_dict.items() if value%2==0 if value>=30}
print(new_dict)
new_dict={person:('old' if age>=50 else 'young') for (person,age) in original_dict.items()}
print(new_dict)

#Printable representation of any custom object
class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return repr('Hello '+self.name)

person=Person("Adam")
print(repr(person))

#Reversal of custom object iterator
class Vowel:
    vowel=['a','e','i','o','u']
    def __reversed__(self):
        return list(reversed(self.vowel))

vo=Vowel()
print(reversed(vo))


#sorted list based on tuple comparison using sorted() function
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]
def sorted_participant(item):
    marks=100 - item[1]
    age=item[2]
    return (marks,age)

print(sorted(participant_list,key=sorted_participant))




