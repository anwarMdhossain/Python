#getattr() function use

class Person:
    name="Anwar"
    sex="Male"
    age=31
    
person=Person()
print("Name of the person ",getattr(person,"name","Benami"))
print("Sex of {} is {}".format(getattr(person,"name"),getattr(person,"sex")))
print("{} is {} year old".format(getattr(person,"name"),getattr(person,"age")))
print("He is residing at ",getattr(person,"addr","Durgapur"))

#Two built-in functions isinstance() and issubclass() are used to check inheritances.
#The function isinstance() returns True if the object is an instance of the class or other classes derived from it.
#Each and every class in Python inherits from the base class "object".

class Browser:
    #protected class attribute
    _no_of_webpages = 0
    def __init__(self,page):
        self._page = page
        self.incognito = False
        Browser._no_of_webpages+=1

    #factory method
    @classmethod
    def with_incognito(cls,cog_page):
        instance = cls(cog_page)
        instance.incognito=True
        return instance

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self,new_page):
        if type(new_page) is not str:
            raise NameError("Page is not correct")
        self._page=new_page

    @staticmethod
    def get_browser_info():
        return {"Name": "Google Chrome","Version":"96.0.4664.110","OS": "Windows"}

bw=Browser("Scalar.com")
print(bw.get_browser_info())
