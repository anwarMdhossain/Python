#Example of for loop
for letter in "python":
    print("Character is: ",letter)
for num_list in [10,20,30,40,50]:
    if num_list==30:
        continue
    else:
        print("Number is: ",num_list)
        
#Example of while loop/Break
count=1
while count<=4:
    if count==3:
        break
    else:
        print("Present count is: ",count)
    count=count+1
print("Good Bye")

#for loop with else block
#Else block is executed when items are exhausted from the iterable object
fruits=["Apple","Lichi","Mango","Orange"]
for fr in fruits:
    print("I like",fr)
else:
    print("Fruit list got exhausted")

#while loop with else block
result=0
num=int(input("Enter the counter number: "))
while num!=0:
    result=result+num**2
    num -=1
else:
    print("Summation is",result)
