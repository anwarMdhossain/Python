grocery = ['bread', 'milk', 'butter']
print(list(enumerate(grocery)))

for gr in list(enumerate(grocery)):
    print(gr)

print("\n")

for index,item in list(enumerate(grocery,start=10)):
    print(index,item)
	
print("\n")

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

result =zip(name,roll_no)
#print(tuple(result))

'''for i in result:
    print(i)'''

for i,(std_name,roll) in enumerate(result):
    print(i,std_name,roll)

print("\n")

#zip to iterables into a single dictionary
dict1={name: roll_no for (name,roll_no) in zip(name,roll_no)}
print(dict1)

#unzip
list_result =list(zip(name,roll_no))
namez,rollz =zip(*list_result)
print(namez)
print(rollz)
