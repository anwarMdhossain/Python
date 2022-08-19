#Selection sort using min()

n=int(input("How many numbers in the list you want? "))
num=[int(input("Enter number: ")) for x in range(n)]
print("Original:",num)

for i in range(len(num)-1):
    min_val=num[i]
    for j in range(i+1,len(num)):
        if num[j]<min_val:
            min_val=num[j]
    min_ind=num.index(min_val,i)
    print("Min_val",min_val,"present at",min_ind,"index")
    if num[i]!=num[min_ind]:
        num[i],num[min_ind]=num[min_ind],num[i]
    print(f"step{i}: {num}")

print("Sorted:",num)


#Bubble or sinking sort
n=int(input("How many numbers in the list you want? "))
num=[int(input("Enter number: ")) for x in range(n)]
print("Original:",num)

for j in range(len(num)-1):
    for i in range(len(num)-1-j):
        if num[i]>num[i+1]:
            num[i],num[i+1]=num[i+1],num[i]
    print(f"step{j}: {num}")

print("Sorted:",num)


#Insertion sort
n=int(input("How many numbers in the list you want? "))
num=[int(input("Enter number: ")) for x in range(n)]
print("Original:",num)

for i in range(1,len(num)):
    key=num[i]
    pos=i-1
    while pos>=0 and key<num[pos]:
        num[pos+1],num[pos]=num[pos],key
        pos=pos-1
    print(f"step{i}: {num}")

print("Sorted:",num)



