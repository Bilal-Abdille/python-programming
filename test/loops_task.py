# task1
# Write a program that displays a numbers 1 to 50 inside a list.

numbers_list = []
for i in range(1,51):
    numbers_list.append(i)

print(numbers_list)




# task2
# From 1 above display the ones divisible by 7 or 5 inside a list.

numbers_list = []
for i in range(1,51):
    numbers_list.append(i)
   # print(numbers_list)

    # divisible by 7 or 5
digits = []

for i in numbers_list:
    if i % 7 ==0 or i % 5 ==0:
        digits.append(i)
print(f"{digits} digits")

# y = range(1,51)
# for i in y:
#     print(i)

# div_by7_or5 =[]
# for num in y:
#     if num %7==0 or num % 5==0:
#         div_by7_or5.append(num)

# for number in div_by7_or5:
#     print(number)

# task3
# Find sum and average of values in the range between 10 to 40.


values= []
for i in range(10,41):
    values.append(i)
print(values)

summation = sum(values)
average = summation / len(values)

print(f"{summation} sum")
print(f"{average} average")

# task4
# Put in a list the first 10 odd numbers between 10 to 50. 

start_value = 10
end_value = 50

# initialize an empty list for odd numbers
main = []


for num in range(10,51):
    if num % 2 !=0:
        main.append(num)
        if len(main) == 10:
            break
print("list of the first 10 odd numbers between 10 to 50:")
print(main)