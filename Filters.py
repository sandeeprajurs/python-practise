def even_check(num):
	if num % 2 == 0:
		return True
	else:
		return False

print even_check(35)

lst = [0,1,2,3,4,5,6,7,8,9]		  #function >> should return boolean
print filter(even_check, lst)     #filter(function_name, list) >> returns list of all filtered values

print filter(lambda num: num%2 ==0, lst)
print filter(lambda num: num>3 , lst)