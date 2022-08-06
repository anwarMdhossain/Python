#Derived class from dict

class loggingdict(dict):
    def __setitem__(self, key, value):
        print(f'Setting {key} : {value}')
        super().__setitem__(key,value)

    def __getitem__(self, key):
        print(f'Fetching {key}')
        super().__getitem__(key)

    def __delitem__(self, key):
        print(f'Deleting {key}')
        super().__delitem__(key)

ld=loggingdict()
ld['India']='Delhi'
ld['Bangladesh']='Dhaka'
ld['India']

del ld['Bangladesh']
ld['Bangladesh']

