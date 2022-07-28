class Test:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30

    #method uses private variable __c
    def print_variable(self):
        print("Value of private varicle is",self.__c)

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.a="Overridden"
        self._b = "Overridden"
        self.__c = "Overridden"

obj=Test()
print(obj.a)
print(obj._b)
print(dir(obj))
#data mangling
print(obj._Test__c)

objext=ExtendedTest()
print(objext.a)
print(objext._b)
print(dir(objext))
#data mangling
print(objext._Test__c)
print(objext._ExtendedTest__c)
obj.print_variable()
objext.print_variable()