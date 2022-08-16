import sqlite3
from employee import Employee

#conn=sqlite3.connect("employee.db")
conn=sqlite3.connect(":memory:")
cur=conn.cursor()
cur.execute("""CREATE TABLE EMPLOYEES (FIRST_NAME TEXT,
                                      LAST_NAME TEXT,
                                      AGE   INTEGER,
                                      SALARY INTEGER)""")

emp1 = Employee("Anwar", "Hossain", 32, 60000)
emp2 = Employee("Junaina", "Parvin", 31, 45000)
emp3 = Employee("Manwar", "Hossain", 39, 150000)
emp4 = Employee("Sabina", "Yeasmin", 39, 50000)

#New record insertion function/method
def insert_employee(emp_obj):
    with conn:
        for obj in emp_obj:
            # print(obj.fname,obj.lname,obj.age,obj.salary)
            # cur.execute("INSERT INTO EMPLOYEES VALUES('{}','{}',{},{})".format(obj.fname,obj.lname,obj.age,obj.salary))
            # cur.execute("INSERT INTO EMPLOYEES VALUES(?,?,?,?)",(obj.fname, obj.lname, obj.age, obj.salary))
            cur.execute("INSERT INTO EMPLOYEES VALUES(:fname,:lname,:age,:salary)",
                    {'fname': obj.fname, 'lname': obj.lname, 'age': obj.age, 'salary': obj.salary})

#Record selection function/method
def select_employee(salary):
    cur.execute("SELECT * FROM EMPLOYEES WHERE SALARY>?",(salary,))
    return cur.fetchall()

#Existing ecord updation function/method
def update_employee(emp_fname,emp_lname):
    with conn:
        cur.execute("UPDATE EMPLOYEES SET AGE=40 WHERE FIRST_NAME=? AND LAST_NAME=?",(emp_fname,emp_lname))
    return cur.rowcount

#Existing record deletion function/method
def delete_employee(emp_lname):
    with conn:
        cur.execute("DELETE FROM EMPLOYEES WHERE FIRST_NAME=:fname",{'fname':emp_lname})
    return cur.rowcount

insert_employee((emp1, emp2, emp3, emp4))
emp_record=select_employee(15000)
print(emp_record)
emp_updated=update_employee('Manwar','Hossain')
print(emp_updated," employee updated")
emp_record=select_employee(15000)
print(emp_record)
emp_deleted=delete_employee('Sabina')
print(emp_deleted," employee deleted")
emp_record=select_employee(15000)
print(emp_record)


#cur.execute("SELECT * FROM EMPLOYEES WHERE AGE>?",(32,))
#returns list of tuples
#print(cur.fetchall())
#print(cur.fetchone())
#conn.commit()
#conn.close()