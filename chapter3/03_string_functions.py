# len()
name = "kunal"
print(len(name))

print(name.startswith("k")) # True
print(name.startswith("K")) # False

print(name.endswith("l")) # True
print(name.endswith("L")) # False

print(name.islower()) # True
print(name.isupper()) # False

name2 = "KUNAL"
print(name2.isupper()) # True

name3 = "Kunal"
print(name3.isupper()) # False
print(name3.islower()) # False because it contains both uppercase and lowercase letters. For a string to be considered lowercase, all characters must be in lowercase. In this case, 'K' is uppercase, so the string does not meet the criteria for being lowercase.
print(name3.isalpha()) # True because it contains only alphabetic characters and no digits or special characters.

name4 = "kunal123"
print(name4.isalnum()) # True because it contains only alphanumeric characters (letters and digits) and no spaces or special characters.

print(name4.isalpha()) # False because it contains digits, which are not alphabetic characters.

# count()
a = "kunalkavathekar"
print(a.count("k")) # 3 - count() is use to count the number of occurrences of a substring in a string. In this case, it counts how many times the letter "k" appears in the string "kunalkavathekar". The output is 3 because there are three occurrences of "k" in the string.

b = "kunalkunalkunalsdfkunalkfunalkunalsdfkunalkunalkunalkunalkunalkunalkunalkunalk"
print(b.count("kunal")) #13

k = "kunal"
print(k.capitalize()) # Kunal - capitalize() is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. In this case, it converts "kunal" to "Kunal" by capitalizing the first letter 'k' and keeping the rest of the letters in lowercase.

k = "KUNAL"
print(k.capitalize()) # Kunal - capitalize() converts the first character 'K' to uppercase (which it already is) and converts the rest of the characters 'UNAL' to lowercase, resulting in "Kunal".

k = "kUnAl"
print(k.capitalize()) # Kunal - capitalize() converts the first character 'k' to uppercase and converts the rest of the characters 'UnAl' to lowercase, resulting in "Kunal".


text = "Kunal Kavathekar is a Python Programmer."
print(text.find("Python")) # 22 - find() is used to find the index of the first occurrence of a substring in a string. In this case, it finds the index of the substring "Python" in the string "Kunal Kavathekar is a Python Programmer.". The output is 22 because the substring "Python" starts at index 22 in the given string.


print(text.replace("Python", "Java")) # Kunal Kavathekar is a Java Programmer. - replace() is used to replace occurrences of a substring with another substring in a string. In this case, it replaces the substring "Python" with "Java" in the string "Kunal Kavathekar is a Python Programmer.". The output is "Kunal Kavathekar is a Java Programmer." because the word "Python" has been replaced with "Java".
print(text) # Kunal Kavathekar is a Python Programmer. - The original string remains unchanged because strings in Python are immutable, meaning that any operation that modifies a string will create a new string rather than changing the original string.

text2 = text.replace("Python", "Java")
print(text2) # Kunal Kavathekar is a Java Programmer. - The new string with the replacement is stored in the variable text2, while the original string text remains unchanged.
print(text) # Kunal Kavathekar is a Python Programmer. - The original string text is still unchanged, demonstrating the immutability of strings in Python.

print(text.split()) # ['Kunal', 'Kavathekar', 'is', 'a', 'Python', 'Programmer.'] - split() is used to split a string into a list of substrings based on a specified delimiter. In this case, it splits the string "Kunal Kavathekar is a Python Programmer." into a list of words using the default delimiter (space). The output is a list of individual words from the original string.

text3 = "Kunal,Kavathekar,is,a,Python,Programmer."
print(text3.split(",")) # ['Kunal', 'Kavathekar', 'is', 'a', 'Python', 'Programmer.'] - In this case, it splits the string "Kunal,Kavathekar,is,a,Python,Programmer." into a list of substrings using the comma (,) as the delimiter. The output is a list of individual words from the original string, separated by commas.

list = ['Kunal', 'Kavathekar', 'is', 'a', 'Python', 'Programmer.']
text4 = " ".join(list)
print(text4) # Kunal Kavathekar is a Python Programmer. - join() is used to concatenate a list of strings into a single string, with a specified separator between each element. In this case, it joins the list of words ['Kunal', 'Kavathekar', 'is', 'a', 'Python', 'Programmer.'] into a single string with a space (" ") as the separator. The output is "Kunal Kavathekar is a Python Programmer." which is the original string before it was split into a list.


print("123".isdigit()) # True - isdigit() is used to check if all characters in a string are digits. In this case, the string "123" consists entirely of digits, so the output is True.

print("     ".isspace()) # True - isspace() is used to check if all characters in a string are whitespace characters (spaces, tabs, newlines, etc.). In this case, the string consists entirely of spaces, which are considered whitespace characters, so the output is True.

print(" sdf ".isspace()) # False - In this case, the string " sdf " contains non-whitespace characters (the letters 's', 'd', and 'f'), so the output is False because not all characters in the string are whitespace characters.