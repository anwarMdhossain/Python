#Regular expression practice 

import re

string="Geeks. for Geeks"
match=re.search(r"\.",string)
print(match.start(),match.end())

string1 = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
match=re.findall("\d+",string1)
print(match)

pattern=re.compile(r"ab?")
match=pattern.findall("ababbaabbbaaabbbbbbb")
print(match)

pattern=re.compile(r"\W+")
val=pattern.split("Words, words , Words")
print(val)
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 5))

print(re.sub("ub","ib","Subject has booked a Uber already",flags=re.IGNORECASE))
tup1=re.subn("ub","ib","Subject has booked a Uber already",count=2,flags=re.IGNORECASE)
print(tup1)
print(tup1[1])

matched_obj=re.search("([a-zA-z]+) (\d+)","I was born on 26th July 1990")
print(matched_obj.group())
print(matched_obj.group(1))
print(matched_obj.group(2))
print(matched_obj.re)
print(matched_obj.string)
print(matched_obj.span())

s = "Welcome to GeeksForGeeks"

# here x is the match object
res = re.search(r"(\D{2} G)", s)

print(res.group())