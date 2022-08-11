#pattern printing using python prgramming

#Example 1
n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range(0,i):
        print(end=" ")
    for k in range(1,n-i+1):
        print("*", end=" ")
    print()
	
#Example 2
n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for k in range(1,2*i+1):
        print("*",end=" ")
    print()
	
#Example 3
n=int(input("Enter the number of lines: "))
k=1
for _ in range(1,n+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k+=2
    print()
	
#Example 4
n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
	
#Example 5
def pyramid_start(row):
    for i in range(row):
        print(" "*(row-i-1)+"* "*(i+1))
    for j in range(row-1,0,-1):
        print(" "*(row-j)+"* "*(j))

pyramid_start(10)

#example 6:
n = int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()