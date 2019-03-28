# try:
# 	f = open ('testfile1232.txt', 'w')
# 	f.write('Test write this')

# except:
# 	print 'There was an error!'

# finally:
# 	print "Always execute finally code blocks!"

def askint():
	
	while True:
		try:
			val = int(raw_input("Please enter an integer:"))

		except:
			print 'Looks loke you didnt enter an integer!'
			continue

		else:
			print 'Correct that is an integer'
			break
			
		finally:
			print 'Finally block executed'

		print val

askint()