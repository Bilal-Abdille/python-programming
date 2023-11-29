# # Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should
#  print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points.
# # For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.


# speed = int(input("Enter the speed of the car: "))

# speed_limit = 70
# demerit_point = 12

# if speed<= speed_limit:
#     print("Ok")
# else:
#     demerit_point = (speed- speed_limit)//5

#     print("points", demerit_point)

#     if demerit_point > demerit_point:
#         print("license suspended.")



speed = int(input("Enter the speed of the car: "))

speed_limit = 70
demerit_point =0

if speed <=speed_limit:
    print("ok")
elif(speed>speed_limit and speed<75):
    demerit_point = 1
else:
    demerit_point = round((speed-speed_limit)/5)
    if demerit_point >12:
        print("license is suspended")
    else:
        print(f"demerit points {demerit_point}")

        print(demerit_point)