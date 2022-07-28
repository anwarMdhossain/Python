#Regular Expression example
import re

pattern="\d+"
pattern1="\s"
rep_str =''
test_string='Hello? 12 Hi: 13 Bonjour[ 14'
result=re.findall(pattern,test_string)
#split(pattern,string,maxsplit)
spl_result=re.split(pattern,test_string,2)
#sub(pattern,replace,string,count="no of replace happens)
new_string=re.sub(pattern1,rep_str,test_string,2)
#subn(pattern,replace,string,count="no of replace happens) with returning tuple
new_string1=re.subn(pattern1,rep_str,test_string)
if result:
    print("Found", result)
    print(spl_result)
    print(new_string)
    print(new_string1)
else:
    print("Not found")
    print(spl_result)


#Basic of search() method under re module
import re

pattern="(\d{2}) (\d{4})"
test_string="23423 4567. 34567 23 34534 345"
result=re.search(pattern,test_string)

print(result.group())
#print whole group pattern
print(result.group(0))
#print first group
print(result.group(1))
#print second group
print(result.group(2))
print(result.group(1,2))
print(result.groups())
print(result.start())
print(result.end())
print(result.span())
print(result.re)
print(result.string)

#To print raw string withour escape characters
import re
#\t and \n are excape characters
test_string="\nPython is wonderful language.\t it is very easy to learn"
result=re.findall(r'[\n\t\r]',test_string)
print(test_string)
print(result)

