f = open('C:\Users\sandeep\Desktop\New Text Document.txt')
# print f.read()
# # print f.read()   //Wont read second time as cursor is at the bottom of the page, so we use seek(0) to bring cursor to first line   
# f.seek(0)
# print f.read()

print f.readlines()    # return each line in list view

for line in open('C:\Users\sandeep\Desktop\New Text Document.txt'):
	print line
