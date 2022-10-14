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


#Merge Sort
def mergeSort(num):
    #to check the length of array
    if len(num)>1:
        mid=len(num)//2
        lnum=num[:mid]
        rnum=num[mid:]

        #cll merge function recursive until we get the base containing one item
        mergeSort(lnum)
        mergeSort(rnum)

        #initialize three variables for 1 pointer of each array and 1 pointer for final array
        i=j=k=0

        while i<len(lnum) and j<len(rnum):
            if lnum[i]<rnum[j]:
                num[k]=lnum[i]
                i += 1
            else:
                num[k] = rnum[j]
                j += 1
            k +=1

        while i<len(lnum):
            num[k]=lnum[i]
            i +=1
            k +=1

        while j<len(rnum):
            num[k]=rnum[j]
            j +=1
            k +=1

if __name__=="__main__":
    n=int(input("How many numbers in the list you want? "))
    num=[int(input("Enter number: ")) for x in range(n)]
    print("Original:",num)
    mergeSort(num)
    print("Sorted:",num)
	
	
#QuickSort
def quickSort(num,low,high):
    if low<high:
        part=partition(num,low,high)
        #call quickSort function recursively until we get the base containing one item
        quickSort(num,low,part-1)
        quickSort(num,part,high)

def partition(num,low,high):
    pivot=num[high]
    pos=low-1
    for i in range(low,high):
        if num[i]<=pivot:
            pos +=1
            num[pos],num[i]=num[i],num[pos]
    num[pos+1],num[high]=pivot,num[pos+1]
    return pos+1


if __name__=="__main__":
    n=int(input("How many numbers in the list you want? "))
    num=[int(input("Enter number: ")) for x in range(n)]
    print("Original:",num)
    quickSort(num,0,len(num)-1)
    print("Sorted:",num)
	

#Quick Sort
import random
import statistics

def pivot_position(list1,first,last):
    #rand_val=random.randint(first,last)
    #list1[rand_val],list1[last]=list1[last],list1[rand_val]
    middle=(first+last)//2
    piv=statistics.median([first,last,middle])
    list1[piv], list1[last] = list1[last], list1[piv]
    pivot_val=list1[last]
    left =first
    right=last-1
    while True:
        while left<=right and list1[left]<=pivot_val:
            left=left+1
        while left<=right and list1[right]>=pivot_val:
            right=right-1

        if left>right:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left] = list1[left],list1[last]
    return left


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





