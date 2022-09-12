class Infinte:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        result=self.num
        self.num +=2
        return result

    __call__=__next__

iter_obj=iter(Infinte(),33)

for i in iter_obj:
    print(i)

*****************************************
#Do while loop in Python

list1=["A","B","C","D"]

for _ in iter(int,1):
    if "D" not in list1:
        print("D is not there in list")
    else:
        print("Alphabet found")
        break

**********************************************
#Generator function example with execution time
import random
import time,memory_profiler

names=["Anwar","Junaina","Manwar","Rose","Aaban","Arshiya","Azhar"]
stream=["Science","Arts","Commerce","FashionDesign","Astrology","Psychology"]

def get_list(number):
    list1=[]
    for x in range(number):
        student={
                    "id" : x,
                    "name" : random.choice(names),
                    "dept" : random.choice(stream)
                }
        list1.append(student)
    return list1

def get_generator(number):
    for x in range(number):
        student = {
            "id": x,
            "name": random.choice(names),
            "dept": random.choice(stream)
        }
        yield student

if __name__=="__main__":
    print("Before execution {}MB memory is used".format(memory_profiler.memory_usage()))
    t1=time.time()
    data_list=get_list(1000000)
    t2=time.time()
    print("After execution {}MB memory is used".format(memory_profiler.memory_usage()))
    print("Time taken {} for execution".format(t2-t1))
    '''print(next(get_generator(1000000)))
    t2 = time.time()
    print("After execution {}MB memory is used".format(memory_profiler.memory_usage()))
    print("Time taken {} for execution".format(t2-t1))'''
