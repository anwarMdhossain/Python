def armstrong_number(num):
    result=0
    num_org = num
    length=len(str(num))
    for i in range(len(str(num))):
        digit=num%10
        result=result+digit**length
        num=num//10

    if result==num_org:
        print("Given number is armstrong")
    else:
        print("Given number is not armstrong")

if __name__=="__main__":
    num=int(input("Please enter the number to be checked: "))
    armstrong_number(num)
