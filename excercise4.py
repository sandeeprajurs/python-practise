def ask():
	while True:
		try:
			val = int(raw_input('Input an integer: '))

		except:
			print 'An error occured plese try again'

		else:
			print 'Thank you , your number squared is {x}'.format(x=val**2)
			break

ask()

