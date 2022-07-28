#closure
'''rules:
    1.there must be a nested function
    2.nested function must use argument from enclosing function
    3.enclosing function must return nested function'''

def enclosing_func(msg):
    def inner():
        print(msg)
    return inner

if __name__=='__main__':
    return_func=enclosing_func("Hello Python")
    return_func()
