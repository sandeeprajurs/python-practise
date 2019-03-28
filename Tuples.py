#Tules are similar to lists but they are immutable and they are covered with  braces and comma seperated
tuples = (1, 2, 3, 4, 5)
print tuples

new_tuple = (1, 'sandeep', 'raj', 1.324)
print new_tuple
print len(new_tuple)
print new_tuple[1]
print new_tuple[2:] #can also perfom slicing same as list
print new_tuple.index(1)
print new_tuple.count('sandeep')

awesome_tuple=tuples+new_tuple
print awesome_tuple

tuple_dict = ({'name':'sandy'})          #tuple can hold dictionaries and list
print tuple_dict

tuple_list = ([1,2,3])
print tuple_list

# tuples[0] = 123  #TypeError: 'tuple' object does not support item assignment
