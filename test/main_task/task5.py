input1= float(input("Enter the first number: "))
input2= float(input("Enter the second number: "))
input3= float(input("Enter the third number: "))

#compare the inputs to find the largest
largest = input1

if input2 > largest:
    largest = input2

if input3 > largest:
    largest = input3

    # print the result
print("The largest number is:", largest)