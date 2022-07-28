#**args,**kwargs
#sequence of argument passing would be standard,*args,*kwargs

sample_dict={"One":1,"Two":2,"Three":3,"Four":4}

for keyitems in sample_dict.items():
    print(keyitems)

def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result

print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
 
printingData('007', 'agent', firstName='James', lastName='Bond') 

#unpacking operator(* -> for iterable,**--> dictionary)

list1=["Hello","My","dear","Pyhton"]
print(*list1)

techStackOne = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStackTwo = {"Python" : "ABC"}
merged={**techStackOne,**techStackTwo}
print(merged)
