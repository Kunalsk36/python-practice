num = int(input("Enter a number: "))
z = int(input("Enter a number for division: "))
if(z == 0):
    print("Division by zero is not allowed.")
else:
    remainder = num % z
    print("The remainder is: " + str(remainder))