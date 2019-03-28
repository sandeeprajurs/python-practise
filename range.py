print range(10)     #range(stop)   range(start,stop[,steps])     range returns list

x = range(10)
print type(x)     #gives the data type of obj

print range(0,10)


#xrange() >> If i want to get range of very large number then i use it, xrange wont save numbers in memory

y = xrange(0,99)
print type(y)

# casting xrange to list 
print list(y)