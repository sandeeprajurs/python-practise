#dictionaries are key value pairs enclosed in flower braces
#order is not retained in dictionaries
my_dict = {'key1':'value1', 'key2': 'value2', 'key3':'value3', 'key4':'value4'}
print my_dict

new_dict = {'num':124, 'name':'sandeep', 'obj':6878, 'decimal_name':8.89}
# print new_dict[0]  #Error: key error
print new_dict['num']    #returns the value of values datatype
print new_dict['name'].upper()
print new_dict['name'][2:]       #as it returns string bcs value's datatype is string, I can perform all string related operations

new_dict['num'] = new_dict['num']+124
print new_dict
# or we can do as below(shortcut)
new_dict['num'] += 124
print new_dict['num']

d = {}
d['a'] = 'sandeep'
d['b'] = 'rashmi'
print d

# Nested dictionaries
nested_dict = {'k1': {'nestkey':{'subnestkey':'value'}}}      #We can also have lists inside inside dictionaries
print nested_dict['k1']['nestkey']['subnestkey'] 

#dictionarie inbuilt methods
print d.keys()
print d.values()
print d.items()       #return keys and values in the form of tuples


#Tricky dict
d = {'k1':[1,2,{'k2':['this is tricky', {'toughie': [1,2,['hello']]}]}]}

print d['k1'][2]['k2'][1]['toughie'][2][0]
d.sort()