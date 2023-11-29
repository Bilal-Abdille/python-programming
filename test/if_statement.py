# Take three inputs from a user, separately. Print the largest of the numbers.
    # Hint: Determine what type of data is taken in as input
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1>num2 and num1>num3:
#     print( f" {num1} :number 1 is the lasrgest number ")
# elif num2>num1 and num2>num3:
#     print(f"{num2} :number 2 is the largest number  " )
# else:
#     print(f"{num3} :number 3 is the largest  number " )

    #task 2
    # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
    #  otherwise display “Normal temperature
temp = float(input("enter your tempreture: "))
if temp >30:
     print("the tempreture is too high")
elif temp<15.5:
     print("the tempreture is too low")
else:
     print("the tempreture is normal")