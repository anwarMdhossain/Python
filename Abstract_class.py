'''We can make abstract classes in Python using abc module of Python
We can implement abstract classes by inheriting the ABC class
We use @abstractmethod decorators to define abstract methods in Python
Abstract classes help to provide the blueprint for another class
Abstract classes may contain concrete methods
Abstract classes cannot be instantiated
Abstract classes ensure that our software is flexible enough to support future changes'''

from abc import ABC,abstractmethod,abstractproperty

class Shape(ABC):
	def __init__(self,shape_name):
		self.shape_name=shape_name

	@abstractmethod
	def draw(self):
		print("Lets print the canvas")
	@abstractproperty
	def name(self):
		pass

	def print_greetings(self):
		print("Hello from Abstract class")

class Circle(Shape):
	def __init__(self):
		super().__init__("cirle")
	def draw(self):
		super().draw()
		print("Drawing a circle")
	@property
	def name(self):
		return self.shape_name
c=Circle()
c.draw()
c.print_greetings()
print(f"Shape name is {c.shape_name}")

try:
	s=Shape("Generic shape")
except Exception as e:
	print(e)
