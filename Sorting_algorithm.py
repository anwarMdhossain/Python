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

#Quick sort
#Insertion sort
def pivot_position(list1,first,last):
    pivot_val=list1[first]
    left =first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot_val:
            left=left+1
        while left<=right and list1[right]>=pivot_val:
            right=right-1

        if left>right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right] = list1[right],list1[first]
    return right


def quick_sort(list1,first,last):
    if first<last:
        pivot=pivot_position(list1,first,last)
        quick_sort(list1,first,pivot-1)
        quick_sort(list1,pivot+1,last)


n=int(input("How many numbers in the list you want? "))
num=[int(input("Enter number: ")) for x in range(n)]
print("Original:",num)
length=len(num)
quick_sort(num,0,length-1)
print(num)



