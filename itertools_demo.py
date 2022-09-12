import itertools,operator

'''counter=itertools.count(start=5,step=-2.5)
print(next(counter))
print(next(counter))
print(next(counter))'''

'''data =[100,200,300,400]
cycle=itertools.cycle(data)
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))'''

'''repeat=itertools.repeat(4*3-2,times=5)
print(next(repeat))
print(next(repeat))
print(next(repeat))
print(next(repeat))
print(next(repeat))
print(next(repeat))'''

#daily_data=zip(itertools.count(),data)
#Zip works until shortest iterable gets exhausted
#daily_data=zip(range(10),data)
#itertools.zip_longest works until highestiterable gets exhausted
'''daily_data=itertools.zip_longest(range(10),data)
print(daily_data)
print(list(daily_data))
for index in daily_data:
    print(index)'''

'''cube=map(pow,range(10),itertools.repeat(3))
print(list(cube))'''

'''squares=itertools.starmap(pow,[(0,1),(1,1),(2,1),(3,1)])
print(list(squares))'''

vowels=['a','e','i','o','u']
primenumbers=[3,5,7,11,13]
names=['Md','Anwar','Hossain']
selectors = [1,0,0,1,1]
numbers=[1,2,3,6,8,9,10]
#compress=itertools.compress(vowels,selectors)
#filterfalse=itertools.filterfalse(lambda x: x%2==0,numbers)
#dropvalue=itertools.dropwhile(lambda x:x%2==1,numbers)
#takewhile=itertools.takewhile(lambda x: x%2==1,numbers)
#accumulate=itertools.accumulate(numbers,operator.mul,initial=2)
#print(accumulate)
#combination=itertools.combinations(vowels,2)
#permutation=itertools.permutations(vowels,2)
#product_count=0
#product=itertools.product(primenumbers,repeat=3)
#product=itertools.combinations_with_replacement(primenumbers,3)
#combined=itertools.chain(vowels,primenumbers,names)
#islice=itertools.islice(range(10),1,6,2)
'''for result in accumulate:
    print(result)
    #product_count+=1
#print(product_count)'''

'''with open("sample - Copy.log","r") as f:
    header=itertools.islice(f,3)
    for line in header:
        print(line,end='')'''

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

group_state=itertools.groupby(people,lambda x: x['state'])
print(group_state)
#replicate iterables
copy1,copy2 =itertools.tee(group_state)
#iterable should be sorted beforehand
for key,group in copy2:
    #print(key,len(tuple(group)))
    print(key)
    for person in group:
        print(person)
    print()