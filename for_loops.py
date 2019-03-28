# list = [0,1,2,3,4,5]
# for num in list:
# 	print num

# #even numbers in the list
# for num in list:
# 	if num % 2 == 0:
# 		print num

# list_sum = 0
# for num in list:
# 	list_sum += num

# print list_sum

# tuple = (1,2,3,4,5,6)

# for item in tuple:
# 	print tuple[item-1]

# l = [(2,4), (3,6), (8,9)]

# for item in l:
# 	print item

# # TUPLE UNPACKING
# for (t1, t2) in l:
# 	print t1
# 	print t2
# 	print t1+t2

dict = {'k1':'value1', 'k2':'value2', 'k3':'value3', 'k4':'value4'}
for k,v in dict.iteritems():     #use .iteritems() to iterate over both key value simultaneously
	print k
	print v