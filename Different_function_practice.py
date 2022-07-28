import cmath

#comp_num=3+4j
comp_num=eval(input("Enter the number: "))
result=cmath.sqrt(comp_num)
print("Square root of {0} is {1:.2f}+{2:.3f}j".format(comp_num,result.real,result.imag))

integer=-30
floating=-30.334
complex_num=3-5j

print(abs(integer),' ',abs(floating),' ',abs(complex_num))

l=[1,"Mohan",0]
l1=[]
#since 0 is False but '000' is a string zhich is not 0
s='000'
s1=''
result=any(s1)
print(result)
print(all(''))
print(ascii('Pythön is interesting'))
#0b means binary format
print(bin(3))

#non-integer object using __index__() built in function else it throw TypeError exception
class Quantity:
    apple=10
    grapes=5
    banana=6

    def __index__(self):
        return self.apple+self.grapes+self.banana

print(bin(Quantity()))

print(bool({}))
#it takes alzays integer number as input
print(chr(130))
#The code object returned by compile() method can later be called using methods like:
#exec() and eval() which will execute dynamically generated Python code.
code_obj=compile("n1=5\nn2=4\nsum=n1+n2\nprint('Sum:=',sum)","Single_line_program","exec")
exec(code_obj)

x=5
print(callable(x))

def printobj():
        print("Print the message")

obj=printobj
print(callable(obj))

class Person:
    age=31
    def printAge(cls):
        print("Age of the person is ",cls.age)

Person.printAge=classmethod(Person.printAge)
Person.printAge()


#classmethod and static method example
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def dateOfYearCalculate(cls,name,birthyear):
        return cls(name,date.today().year-birthyear)

    @staticmethod
    def FatherAge(name,birthyear,myyear):
        print("I am inside static method!!")
        return Person(name, date.today().year - birthyear+myyear)

    def diplayAge(self):
        print("Age of {} is {}".format(self.name,self.age))

class Parent(Person):
    age=50

pr_obj=Person("Adam",30)
pr_obj.diplayAge()

pr_obj1=Person.dateOfYearCalculate("Steve",1985)
pr_obj1.diplayAge()

prt_obj=Parent.dateOfYearCalculate("Junaina",1990)
print(isinstance(prt_obj,Parent))

prt1_obj=Parent.FatherAge("Fashihuddin",1960,1990)
print(isinstance(prt1_obj,Person))

Parent.FatherAge("Sahanaj",1980,1990)

#dir(object) method
class Person:
    def __dir__(self):
        return ('name','age','salary')

teacher=Person()
print(dir(teacher))

#two arguements numerator and denominator and return tuple of quotient and remainder
print(divmod(3,8))
#it adds a counter to the item of iterable passed.
language=["Python","C","C++","Java"]
print(list(enumerate(language,start=3)))
for item in enumerate(language,10):
    print(item)
for item,value in enumerate(language,10):
    print(item,value)

#staticmethod example
class Calculator:
    def addNumbers(num1,num2):
        return num1+num2

statmethod=staticmethod(Calculator.addNumbers)
#print(statmethod)
sum=statmethod(3,4)
print(sum)


#staticmethod() example
class Dates:
    #constructor of class
    def __init__(self,date):
        self.date=date

    def getDate(self):
        return self.date

    @staticmethod
    def dateFormat(repl_date):
        return repl_date.replace('/','-')

actual_date_obj=Dates('13-06-2022')
actual_date=actual_date_obj.getDate()
mod_date=Dates.dateFormat('13/06/2022')
if actual_date==mod_date:
    print("Both dates are same")
else:
    print("dates are different")

#Iter() method functionality
vowels=['a','e','i','o','u']
iter_obj=iter(vowels)
print(next(iter_obj))
print(next(iter_obj))
print(dir(iter_obj))

class PrintNumber:
    def __init__(self,max=10):
        self.max=max
    def __iter__(self):
        print("Inside Iter method")
        self.num=0
        return self
    def __next__(self):
        if self.num>=self.max:
            raise StopIteration
        else:
            self.num+=1
            return self.num

pr_obj=PrintNumber(3)
pr_iter=iter(pr_obj)
print(pr_iter)
print(next(pr_iter))
print(next(pr_iter))
print(next(pr_iter))
print(next(pr_iter))

#Another Example
class DoubleIt:
    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__
    
my_iter = iter(DoubleIt(), 16)
for x in my_iter:
    print(x)
