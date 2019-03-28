new_list = []
for num in range(10):
	new_list.append(num)
print new_list

list = [ num for num in range(10) ]         
print list

lst = [ num**2 for num in range(10)]
print lst

even_number_list = [number for number in range(0,10) if number%2==0]         #Conditions in list Comprehensions
print even_number_list

celcious = [0, 10, 20.1, 34.5]
farenheit = [(temp*(9/5.0)+32) for temp in celcious]
print farenheit

# Nested list Comprehensions
   # Final result is numm**4 for the range 16
list_num = [ num**2 for num in [num**2 for num in range(16)]]
print list_num

