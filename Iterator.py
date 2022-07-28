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