list = [1, 2, 3]     #lists are covered with square braces with comma seperated values
print list

my_list = [1, 'sandeep', 1.23, "raja"]      #lists can hold any thing, gives me result in the what i have stored
print my_list

# print my_list[0]

# print my_list[1:]

# print my_list[::2]

# print len(my_list)

# print my_list+ ['rashmi']  #can only concatinate lists to lists

# my_list = my_list+ ['rashmi']

# print my_list * 2

# my_list.append("new_string") #appending string to list
# print my_list

# my_list.pop()   #removes last element from list
# print my_list

# my_list.pop(0)
# print my_list

# # my_list[99]   # Error: IndexError: list index out of range

# my_list.sort()   #sorting of list
# print my_list

# new_list = ['a', 'b' , 'z' , 'm'] 
# new_list.reverse()        #reverese the order of list
# print new_list

# #nesting list
# l_1 = [1, 2, 3]
# l_2 = [4, 5, 6]
# l_3 = [7, 8, 9]

# matrix = [l_1, l_2, l_3]   #list within the list is called matrix(nesting data stricture)
# print matrix

# print matrix[1]

# print matrix[1][0]

# first_col = [row[0] for row in matrix] #for every row in the matrix, grab 0th index(column)
# print first_col

# list_tuple = [(1,2,3),(233), {'sandy':'icecreamcandy'}]       #list can hold tuple and dictionaries
# print list_tuple[2]['sandy']

#updating the list
my_list[3] = "rashu"
print my_list