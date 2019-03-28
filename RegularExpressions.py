import re

# patterns = ['term1','term2']
# text = 'This a string with term1, but not term'
# print re.search('hello', 'hello world')  #search gives match object

# for pattern in patterns:
# 	print 'Searchng for "%s" in: \n"%s"' %(pattern,text)

# 	if re.search(pattern, text):
# 		print '\n'
# 		print 'Match was found. \n'
# 	else:
# 		print '\n'
# 		print 'No Match was found.\n' 

#When no match found None is returned

# match = re.search(patterns[0], text)
# type(match)
# print match.start()
# print match.end()

#split in regular expression
# split_term = '@'

# phrase = 'What is your email, is it hello@gmail.com?'
# print re.split(split_term, phrase)

# # findall method in regular expressions
# print re.findall('match', 'Here is one match, here is another match')

# print re.findall('te*', text)  # after t , there can be 0 e or any number of e
# print re.findall('te+', text)  #s followed by 1 or more e
# print re.findall('te?', text)  #t followed by 0 or 1 e
# print re.findall('te{3}', text) # t followed by 3 e
# print re.findall('te{1,3}', text) # t followed by 1 or 3 e
# print re.findall('[te]', text)   #earches either t or e
# print re.findall('t[te]', text) #1 t folowed by n number of t or e


# phrase2 = 'hi i am very, good? to see you! How is.'
# print re.findall('[^,!.?]+', phrase2)  # + here indcates punctuations appears atleast once and ^ to indicate shouldnot be present


phrase3 = 'This is an example sentance'

print re.findall('[a-z]+', phrase3)  #sequence of lower case letters
print re.findall('[A-Z]+', phrase3)  #sequence of upper case letters
print re.findall('[a-zA-Z]+', phrase3) #sequence of lower and upper case letters
print re.findall('[A-Z][a-z]+', phrase3) #one upper case letter followed by lower case letter