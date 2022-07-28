import zipfile

filename="documents.zip"
with zipfile.ZipFile(filename,'r') as zip:
    zip.printdir()
    zip.extract('documents/Photograph.jpg')
    #zip.extractall()
	for file in zip.infolist():
        print(file.filename,file.compress_size,file.file_size,file.compress_type)

******************************************************************************************		
import os

if __name__ == "__main__":
    for (root,dirs,files) in os.walk('D:\Software\Python code\Test', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')		
		for name in files:
            print(os.path.join(root,name))
        for names in dirs:
            print(os.path.join(root,names))

****************************************************************************			
import os,glob

path=os.getcwd()
os.chdir('D:\Software\Python code\Test\A\A1')
path=os.getcwd()
print(glob.glob("D:\Software\Python code\Test\C\[0-9]*.txt"))
#to print recursive files in a chain of directory under parent directory
print(glob.glob("D:\Software\Python code\Test\**\*.txt",recursive=True))
#to accept data one by one through generator object
it=glob.iglob("D:\Software\Python code\Test\**\*.txt",recursive=True)
print(next(it))
print(next(it))

for searched_file in glob.glob("D:\Software\Python code\Test\C\[0-9]?.txt"):
    print(searched_file)			