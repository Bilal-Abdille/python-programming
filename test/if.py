temp = float(input("Enter your tempreture: "))
if(temp>100):
    print("extream tempreture")
elif(temp<=100 and temp>30):
    print("The tempreture is too high")
elif(temp<=30 and temp>15.5):
    print("Normal tempreture")
else:
    print("The tempreture is too low")
