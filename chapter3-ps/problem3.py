# Write a python program to detect a double space in a string.

text = "Hello  Kunal"
print(text.__contains__("  "))

if text.find("  ") != -1:
    print("Double space is detected.")
else:
    print("Double space is not detected.")


# replace the double space with single space
if "  " in text:
    print("Double space is detected.")
    print("Original text: ")
    print(text)
    text = text.replace("  ", " ")
    print("Text after removing double space: ")
    print(text)
else:
    print("Double space is not detected.") 