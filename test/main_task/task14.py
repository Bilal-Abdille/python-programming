# Write a program that takes input of 2 values and adds them. The program should only accept numbers and 
# floats only or otherwise display an error “invalid character entered” and 
# take the user to re-enter the inputs .

# Initialize variables
num1 = None
num2 = None

# Get the first number from user input
while num1 is None:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid character entered. Please enter a number or float.")

# Get the second number from user input
while num2 is None:
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid character entered. Please enter a number or float.")

# Add the numbers and print the result
result = num1 + num2
print("The sum of", num1,"and", num2, "is:", result)