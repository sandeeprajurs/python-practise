class Circle(object):

	#  class object attribute
	pi = 3.142

	def __init__(self, radius = 1):
		self.radius = radius

	def area(self):              #passing self to this method indicates that, these are the methods of Circle Object
		return (self.radius**2) * Circle.pi      #Class object attributs should be accessed by class name

	def set_radius(self, new_radius):
		self.radius = new_radius

	def get_radius(self):
		return self.radius

c = Circle(10)
print c.area()

c.set_radius(24)
print c.area()
print c.get_radius()