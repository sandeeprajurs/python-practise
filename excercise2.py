import string


# def vol(rad):
# 	return (4.0/3.0)*3.142*(rad**3)

# def ran_bool(num, low, high):
# 	if num in range(low, high+1):
# 		return True

# 	else:
# 		return False

# def up_low(s):
# 	upper=0
# 	lower=0
# 	for letter in s:
# 		if letter.isupper():
# 			upper += 1
# 		if letter.islower():
# 			lower += 1
# 	print "upper is {x} lower is {y} ".format(x=upper, y=lower)

# def unique_list(l):
# 	list=[]
# 	for num in set(l):
# 		list.append(num)
# 	print list

# def multiply(numbers):
# 	ans = 1
# 	for num in numbers:
# 		ans = ans*num
# 	print ans

# def palindrome(string):
# 	if string[::-1] == string:
# 		print "{x} is a palindrome".format(x=string)
# 	else:
# 		print "{x} is not a palindrome".format(x=string)

# def ispangram(str1, alphabet=string.ascii_lowercase):
# 	# str1=str1.replace(" ","")
# 	for letter in list(alphabet):
# 		if letter not in str1:
# 			print "'{x}' is not a panagram".format(x=str1)
# 			break
# 	else:
# 		print "'{x}' is a panagram".format(x=str1)


# def ispangram(str1, alphabet=string.ascii_lowercase):
# 	alphaset = set(alphabet)
# 	return alphaset <= set(str1.lower())



# print vol(10)

# print ran_bool(2,1,10)

# up_low("Hi Howe ASKD ARE you")

# unique_list([1,2,3,4,2,2,2,1,1,1])

# multiply([1,2,3,4,5,6])

# palindrome("mom")

# print ispangram("The quick brown fox jumps over the lazy dog")
