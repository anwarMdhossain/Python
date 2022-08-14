with open("Peacock.jpg","rb") as rf:
    with open("copy_peacock.jpg","wb") as wf:
        size_of_file = 4096
        content=rf.read(size_of_file)
        while len(content)>0:
            wf.write(content)
            content = rf.read(size_of_file)

#Print something in a file instead of sys.stdout 
file1=open("D:\Software\Python code\python_txt.txt",'w')
print("Python is wonderful programming language",file=file1)
file1.close()

#file sample program

with open("sample_file.txt","w") as f:
    f.writelines(["Pyhton is awesome!\n","Pyhton is great!"])

with open("sample_file.txt","a") as f:
    f.writelines(["\nPyhton is excellent!\n","Pyhton is fabulous!"])

*************************************************************************************
#context manager using class by implemention __enter__ and __exit__ methods
class Open_file:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with Open_file('D:\Software\Python code\sample_file.txt','a') as f:
    f.write("This is contect manager using class")

print(f.closed)

*************************************************************************************
#context manager using function decorator
from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally:
        f.close()

with open_file('D:\Software\Python code\sample_file.txt','a') as f:
    f.write("\nThis is contect manager example using function decorator")

print(f.closed)
***********************************************************

#directory in Python 
import os
import shutil
current_dir=os.getcwd()
print(current_dir)
print(os.listdir())
#print(os.listdir("practice"))
#os.mkdir("practice\superprac")
#os.chdir("C:\Users\Sohel\PycharmProjects\pythonProject\")
#print(os.getcwd())
#os.rename("practice","Practice")
os.listdir()
#os.remove("sample.txt")
#os.rmdir("Practice")
shutil.rmtree("Practice")

*******************************************************
import os
import shutil

pathname="D:\Software\Python code\pycharm_sample_file.txt"
path="D:\Software\Python code"
directory="False_directory"
path=os.path.join(path,directory)
#os.rmdir(path)
shutil.rmtree(path)

if os.path.isfile(pathname):
    os.remove(pathname)
    print("File removed")
else:
    print("File is not removed")
