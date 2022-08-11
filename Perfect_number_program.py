def perfect_number(num):
    result=0
    for i in  range(1,num):
        if num%i==0:
            result=result+i;

    if result==num:
        print("Given number is Perfect number")
    else:
        print("Given number is not Perfect number")

if __name__=="__main__":
    num=int(input("Please enter the number to be checked: "))
    perfect_number(num)
