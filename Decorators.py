# def hello():
# 	return "hello how are you"

# greet = hello    # assigning hello function to greet variable, 
# print greet()			#great() is independent of hello

# del hello

# print greet()

#----------------------------------------------------------------------

  #Functions with in functions and returnning function
  # if function is written as hello() it executes if written like this >> x = hello it assignes the functon to x

# def hello(name = 'Jose'):

# 	def greet():
# 		return "Greet function given"

# 	def welcome():
# 		return "welcome function given"

# 	if name == 'Jose':
# 		return greet

# 	else:
# 		return welcome

# x = hello('sandeep')
# print x

#----------------------------------------------------------------------

# decorators >>doing manually
def new_decorator(func):

	def wrap_func():
		print "befor executing func"

		func()

		print "after executing func"
	return wrap_func

def function_needs_decorator():
	print "This function needs decorator"

# function_needs_decorator = new_decorator(function_needs_decorator)   #step1
# function_needs_decorator()                                           #step2

#using decorators

@new_decorator                #using decorator will automate step1>>i.e passing func as argument to a function
def function_needs_decorator():
	print "This function needs decorator"

function_needs_decorator()