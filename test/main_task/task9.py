# # Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....


# stars = ""
rows = int(input("Enter the number of rows: "))
# count = 0
# for i in range(rows):
    # stars+="*"
    # count+=1
    # print(stars)
    # if count==rows:
for i in range(1+rows + 1):
     print("* " * i )
    #  print(stars+("." *rows))
