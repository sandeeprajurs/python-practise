class Dog(object):
	# Class object attribute
	species = 'mammel'          #for all dog objects species will be mammel
	def __init__(self, breed, name):  # __init__() instanciate or initilize the attributes of an object 
		self.breed = breed      # self.breed >>> Dog's breed attriute and self is first attribute of the dog class
		self.name = name
		
sam = Dog(breed = 'Lab', name = 'Sammy')
print type(sam)
print sam.breed
print sam.name
sam.species= "animal"
print sam.species


#new dog nstance
nico = Dog(breed = 'Pum', name= 'Nico')
print nico.species      #species will not change per instance, it will always be mammel

