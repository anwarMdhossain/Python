#Here __new__() has been used to control instantiation of class
class Students(object):
    def __init__(self, idNo, grade):
        self._idNo = idNo
        self._grade = grade

    #__new__ method to control instantiation of object
    def __new__(cls, idNo, grade):
        print("Creating Instance")
        instance = super(Students, cls).__new__(cls)
        if 5 <= grade <= 10:
            return instance
        else:
            return None

    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)

stud1 = Students(1, 7)
print(stud1)

stud2 = Students(2, 12)
print(stud2)

***************************************
#to make class iterrable for using in/not in keyword we have to overload __contains__ method
import datetime
class DateClass():
    def __init__(self,startdate,enddate):
        self.startdate =startdate
        self.enddate=enddate
    def __contains__(self, item):
        print("Contains() methiod is being overloaded")
        return self.startdate<=item<=self.enddate

if __name__=='__main__':
    dt=DateClass(datetime.date(2022,1,1),datetime.date(2022,12,1))
    checkdate=datetime.date.today()
    print(checkdate in dt)
    print("Class: ",dt.__class__.__name__,"\n","Attributes: ", dt.__dict__)
	
***************************************
def decorate(power_of_two):
    def wrapper(num):
        return num*power_of_two
    return wrapper

func_obj=decorate("Hello")
print(func_obj(2))
#returns a tuple of cell objects
print(func_obj.__closure__)
print(func_obj.__closure__[0].cell_contents)