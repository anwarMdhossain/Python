#type is default metaclass
#metaclass creates class and class creates object
#__new__() creates object and returns whereas __init__() initialize the object that is passed as arguement

class A:
    pass

A.x=10
A.foo=lambda self : print("Hello Python")

obj=A()
print(obj.x)
obj.foo()

print(type(obj))
print(type(A))

*****************************
#type() takes either one or three arguments

def printMethod(self):
    print("This is a class method")

class Base:
    def baseMethod(self):
        print("This is class method of Base")

#format of type(Name of the dynamic class,(tuple of base classes),class dictionary)
Test = type('Test',(Base,),dict(name="Sammi",dynamic_class_method=printMethod))
print(type(Base))
print(type(Test))
test_obj=Test()
test_obj.baseMethod()
test_obj.dynamic_class_method()
print(test_obj.name)

***************************************
#another example
def init(self,filename):
    self.filename=filename

def getFilename(self):
    return self.filename

Test=type('Test',(object,),{'__init__': init,'dynamic_method_name': getFilename})

def secondFilename(self):
    return 'Sammi.txt'

Test1=type('Test1',(Test,),{'dynamic_method':secondFilename})
test_obj=Test1('Anwar.txt')
print(test_obj.dynamic_method_name())
print(test_obj.dynamic_method())

*******************************************************
#creating a metaclass MultiBases which will check if the class being created has inherited from more than one base class. If so, it will raise an error. 

class MultiBases(type):
    def __new__(cls,classname,bases,class_dict):
        if len(bases)>1:
            raise TypeError("Multiple base classes are inherited!!")
        return super().__new__(cls,classname,bases,class_dict)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A):
    pass

class C(A,B):
    pass

********************************************
#vars() without any argument acts like locals()

class Person:
    def __init__(self,name="Sammi",age="31",profession='Housewife'):
        self.name=name
        self.age=age
        self.profession=profession

    def printMessage(self):
        print("{} is {} aged {}".format(self.name,self.profession,self.age))

    def loc(self):
        a=10
        return locals()

    def code(self):
        a=20
        return vars()

    def prog(self):
        a=30
        return vars(self)

pr=Person()
print(pr.__dict__)
print(vars(pr))

print(pr.loc())
print(pr.code())
print(pr.prog())

********************************************

import functools

def decorateMethod(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(func.__qualname__,"is called****")
        result=func(*args,**kwargs)
        return result
    return wrapper

def decorateClass(cls):
    for key,value in vars(cls).items():
        if callable(value):
            setattr(cls,key,decorateMethod(value))
    return cls

@decorateClass
class Calc:
    def add(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        try:
            if y==0:
                raise ZeroDivisionError("Please check denominator value")
            else:
                return x/y
        except ZeroDivisionError as ze:
            print(ze)

cl_obj=Calc()
print("Addition Value is:",cl_obj.add(2,3))
print("Multiplication Value is:",cl_obj.mul(2,3))
print("Divion Value is:",cl_obj.div(2,0))

***************************************************
#Using metaclasses

import functools

def decorateMethod(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(func.__qualname__,"is called****")
        result=func(*args,**kwargs)
        return result
    return wrapper

def decorateClass(cls):
    for key,value in vars(cls).items():
        if callable(value):
            setattr(cls,key,decorateMethod(value))
    return cls

class Metaclass(type):
    def __new__(cls, classname,baseclass,class_dict):
        obj=super().__new__(cls, classname,baseclass,class_dict)
        obj=decorateClass(obj)
        return obj

class Base(metaclass=Metaclass):
    pass

class Calc(Base):
    def add(self,x,y):
        return x+y

class Adv_calc(Calc):
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        try:
            if y==0:
                raise ZeroDivisionError("Please check denominator value")
            else:
                return x/y
        except ZeroDivisionError as ze:
            print(ze)

cl_obj=Adv_calc()
print("Addition Value is:",cl_obj.add(2,3))
print("Multiplication Value is:",cl_obj.mul(2,3))
print("Divion Value is:",cl_obj.div(5,2))

*****************************************************************

class Meta(type):
    def __new__(self,class_name,bases,attr):
        print(attr)
        dict1={}
        for key,val in attr.items():
            if key.startswith('__'):
                dict1[key]=val
            else:
                dict1[key.upper()]=val
        print(dict1)
        return type(class_name,bases,dict1)

class Dog(metaclass=Meta):
    x=5
    y=10

    def printHello(self):
        return "Hello Python"

d=Dog()
print(d.PRINTHELLO())

