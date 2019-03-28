#sets are unordered collection of unique elemets
x = set()
x.add(1)
x.add(2)
x.add(3)
print x
x.add(2)  #wont add 2 bcs already 2 is present
print x

# casting list's to set's
l = [1,1,1,1,1,2,2,3,3,3,3,4,4,4,4]
print set(l)