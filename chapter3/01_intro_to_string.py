# String is a data type that represents a sequence of characters.

# STRING IS IMMUTABLE: Once a string is created, it cannot be modified. Any operation that seems to modify a string will actually create a new string.

# It is used to store and manipulate text in Python. 
# Strings are enclosed in either single quotes (' ') or double quotes (" ") or triple single quotes (''' '''). For example:

name = "Kunal" # using double quotes
print(name)

name2 = 'Tanvi' # using single quotes
print(name2)

name3 = '''
Kunal 

Tanvi''' # using triple single quotes
print(name3)


nameshort = name[0:3] # slicing the string to get the first three characters
# the 3 in the above code is not included in the output. It will give us 'Kun' as output.
# it will take name[0], name[1], name[2] and will not take name[3]
print(nameshort)

# Kunal 
# 01234
# -5-4-3-2-1

print(name[-1]) # it will give us the last character of the string which is 'l'