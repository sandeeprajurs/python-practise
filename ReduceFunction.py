list = [10,20,30,40,50,34,56,21,13]
print max(list)

max_find = lambda a,b: a if (a>b) else b 

print reduce(max_find,list)
print globals()