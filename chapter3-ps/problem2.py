# Write a python program to fill a letter template given below with name and date.

letter = '''
Dear <|NAME|>,

You are Selected!

<|Date|>

'''

name = input("Enter your name: ")
date = input("Enter the date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)


# modern approach:
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = f'''
Dear {name},

You are Selected!

{date}
'''

print(letter)