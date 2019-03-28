st = "Print only the words that starts with s in this sentence" #use for, split() and if

words = st.split(" ")

for word in words:
	if word[0] == 's':
		print word


# list comprehensions

list = [num for num in range(1,51) if num%3==0 ]
print list

# ex3
st = "Print every word in this sentance that has an even number of letters"

words = st.split(" ")

for word in words:
	if len(word) % 2 == 0:
		print word

# ex4

for num in range(1,101):
	if num % 3 ==0 and num % 5 ==0:
		print "FizzBuzz"
		continue

	if num % 3 == 0:
		print "Fizz"
		continue

	if num % 5 == 0:
		print "Buzz"
		continue

	else:
		print num



# list comprehensions

st = "Create a list of the first letters of every word in this string"

list = [word[0] for word in st.split(" ")]
print list





