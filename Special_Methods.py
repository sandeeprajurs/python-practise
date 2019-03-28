class Book(object):

	def __init__(self, title, author, pages):

		print "A book has been created!"
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):                   #like toString in java
		return "Title: %s, Author: %s, pages %s"%(self.title, self.author, self.pages)

	def __len__(self):
		return self.pages

b = Book('Python', 'Jose', 100)
print b
print len(b)

