class Employee:
    def __init__(self,fname,lname,age,salary):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.salary=salary

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @property
    def employee_details(self):
        return f"Employee Name: {self.fullname}\nEmployee Age: {self.age}\nEmployee Salary:{self.salary}"

    def __repr__(self):
        return f"Employee({self.fname},{self.lname},{self.age},{self.salary})"

