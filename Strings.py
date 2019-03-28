s = "rashmi"

print(s[0])   #indexing

print(s[:])    

print(s[1:5])

print(s[:-1])

print(s[::-1])

print(s[::-2])

print(s[1:4:2])

print(s.upper())

print(s.lower())

#s[0]='d'       Error: Strings are immutable

print(s.split('a'))

print(s + 'awesome')

print(s * 10)        #prints "rashmi" 10 times

print(len(s))

print(s.count('a'))  #counts instances of a

print(s.find('a'))   #Give index of letter

new_string = s.replace('a','z')
print(new_string)

