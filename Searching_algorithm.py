#Binary search
def binarySearch(list1,key):
    left=0
    right=len(list1)-1
    list1.sort()
    print("Sorted list:",list1)
    found = False
    while left <= right and not found:
        mid_index=(left+right)//2
        if key == list1[mid_index]:
            found = True
        elif key > list1[mid_index]:
            left = mid_index + 1
        else:
            right = mid_index - 1

    if found==True:
        print(f"{key} is found at {mid_index}")
    else:
        print(f"{key} is not found!!")


n=int(input("How many numbers in the list you want? "))
num=[int(input("Enter number: ")) for x in range(n)]
print("Original list:",num)

key_val=int(input("Enter the key value to be searched: "))
binarySearch(num,key_val)
