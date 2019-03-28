def fahrenheit(T):
	return (9.0/5)*T + 32

print fahrenheit(0)

temp = [0,22.5,40,100]

print map(fahrenheit, temp)    #map(function_name, list) >>returns list of all computed values

print map(lambda T: (9.0/5)*T + 32, temp)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print map(lambda x,y,z: x+y+z, a,b,c)