import functools
import operator
#  filtering odd square which are divisible by 5
lst=filter(lambda x : x%5==0,[x**2 for x in range(9) if x%2==1])
print(list(lst))

x=functools.reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15])
y=functools.reduce(lambda a,b: a+b, [7, 12, 45, 100, 15])
z=functools.reduce(operator.mul, [7, 12, 45, 100, 15])
print("Greater number is:",x)
print("Summation is:",y)
print("Multiplication of all items:",z)

a=b=5
print("Sum of {0} and {1} is {2}".format(a,b,operator.add(a,b)))
print("Difefrent between {0} and {1} is {2}".format(a,b,operator.sub(a,b)))
print("Multiplication of {0} and {1} is {2}".format(a,b,operator.mul(a,b)))
print("Power of {0} to {1} is {2}".format(a,b,operator.pow(a,b)))
print("Truediv of {0} and {1} is {2}".format(a,b,operator.truediv(a,b)))
#a//b
print("Floordiv of {0} and {1} is {2}".format(a,b,operator.floordiv(a,b)))
#a%b
print("Modulus of {0} and {1} is {2}".format(a,b,operator.mod(a,b)))
print("{0} is greater than {1} is {2}".format(a,b,operator.ge(a,b)))

print("The concatenated product is : ", end="")
print(functools.reduce(operator.add,["Geeks","for","Geeks"]))


**********************************************************************************
import functools
import itertools

lst=[1,2,3,4,5,6,7,8]
print("Actual list is:",lst)
print("Summation of list using reduce(func,sequence) function!!")
#reduce(func,sequence,initial)
print("Result is:",functools.reduce(lambda a,b:a+b,lst,5))

#accumulate returns a list containing intermidiate results.
#Last item in list denotes final result
print("Summation of list using accumulate(sequence,func) function!!")
print("Result is:",tuple(itertools.accumulate(lst,lambda a,b:a+b)))

********************************************************************************
#Reduce() function using three arguements
def reduce(func,sequence,initial=None):
    it=iter(sequence)
    if initial==None:
        value=next(it)
    else:
        value=initial

    for item in it:
        value = func(value,item)
    return value

sg=(2,3,4,5,6,7,8)

result= reduce(lambda a,b:a+b,sg,4)
print("Sum including initial value is :",result)
print("Sum excluding initial value is :",reduce(lambda a,b:a+b,sg))