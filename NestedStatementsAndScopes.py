# name = 'This is a global name'

# def greet():
# 	#Enclosing function
# 	name = "sammy"

# 	def hello():
# 		print "Hello "+name

# 	hello()

# greet()

"""-------------------------------------------------------------------------------------------------------"""

# x= 50
# def func(x):
# 	print "x is", x
# 	x = 2
# 	print "changed local x to ", x

# func(x)
# print "x is still", x

"""-------------------------------------------------------------------------------------------------------"""

x= 50
def func(y):
	# if i had used x before global declaration in a function i will get warning
	global x
	print "x is", x
	x = y
	print "changed global x to ", x

func(2)
print "x is now changed to ", x