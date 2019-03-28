def is_prime(num):
	""" Finds number is prime or not """
	for n in range(2,num):
		if num % n == 0:
			print "%s is not a prime number"%(num)
			break

	else:
		print "%s is a prime number"%(num)

print is_prime(20) #i will get answer and None as function is priniting a value not returnuing
