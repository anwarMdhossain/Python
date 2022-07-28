'''Exception Handling including assert()'''

try:
    string=int(input("Enter the string: "))
    assert type(string)==str,"Given message is not a string!!"

    if type(string)!=str:
        raise TypeError("Type of the input is not correct")
    elif(not string):
        raise ValueError("Value is not True")
except TypeError as te:
    print("Error:",te.__doc__)
except ValueError as ve:
    print("Error:",ve.__doc__)
except AssertionError as ae:
    print(ae)
else:
    print("Operation is successful")