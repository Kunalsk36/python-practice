# Write a python program to display the user entered name follow by Good Afternoon using input function.

inputText = input("Enter a name: ")
outputText = "Good Afternoon " + inputText
print(outputText)

# another way using f-string
outputText = f"Good Afternoon {inputText}"
print(outputText)