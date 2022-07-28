import logging

logging.basicConfig(filename="employee.log",level=logging.DEBUG,format='%(asctime)s:%(lineno)d %(message)s')
logger =logging.getLogger("EmployeeLogger")

class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        logger.debug('Employee created : {}-{}'.format(self.fullName,self.getEmail))
    @property
    def getEmail(self):
        return '{}.{}@gnail.com'.format(self.firstname,self.lastname)

    @property
    def fullName(self):
        return '{} {}'.format(self.firstname,self.lastname)

emp1=Employee('Anwar','Hossain')
emp2=Employee('Junaina','Parvin')

********************************************

import logging
import employee

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("sample.log")
logger.addHandler(file_handler)
formater=logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(lineno)d|%(message)s')
file_handler.setFormatter(formater)
file_handler.setLevel(logging.ERROR)
#logging.basicConfig(filename="sample.log",format='%(levelname)s:%(asctime)s:%(name)s:%(lineno)d|%(message)s',level=logging.DEBUG)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formater)

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    try:
        result=x/y
    except ZeroDivisionError as ze:
        logger.error("Denominator cannot be zero")
        logger.exception("Denominator cannot be zero")
    else:
        return result

logger.debug(add(10,20))
logger.debug(substract(10,20))
logger.debug(mult(10,20))
logger.debug(div(20,0))

********************************

import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_hander=logging.FileHandler("employee.log")
logger.addHandler(file_hander)
formater =logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(lineno)d|%(message)s')
file_hander.setFormatter(formater)

#logging.basicConfig(filename="employee.log",level=logging.INFO,format='%(levelname)s:%(asctime)s:%(name)s:%(lineno)d|%(message)s')

class Employee:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        logger.info('Employee created : {}-{}'.format(self.fullName,self.getEmail))
    @property
    def getEmail(self):
        return '{}.{}@gnail.com'.format(self.firstname,self.lastname)

    @property
    def fullName(self):
        return '{} {}'.format(self.firstname,self.lastname)

emp1=Employee('Anwar','Hossain')
emp2=Employee('Junaina','Parvin')

