class Animal(object):            #base class
	catagory = "mammel"
	def __init__(self):
		print "Animal Created"

	def whoAmiI(self):
		print "Animal"
		return "Animal returned something"

	def eat(self):
		print "Eating"
  
class Dog(Animal):               #derived class or subclass

	def __init__(self):
		Animal.__init__(self)   #Animal.__init__(self) is done automatically by python
		# super(Dog, self).__init__()    >>same as above Animal.__init(self)
		print "Dog Created"

	def whoAmiI(self):
		something = super(Dog, self).whoAmiI()     #if i want to execute animal method or parent class method i use super()
		# something = Animal.whoAmiI(self)         >>both super and calling method by class name are same
		print something     
		print "Dog"

	def bark(self):
		print "woof!"

d = Dog()
d.whoAmiI()   #overrides animals whoami method
d.eat()
d.bark()


