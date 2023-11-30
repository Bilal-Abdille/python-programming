# how to create functions

# def calc_gross(benefits,basic_salary):
#     gross_salary = basic_salary + benefits
#     return gross_salary


# basic_salary = float(input("enter your basic salary: "))
# benefits = float(input("enter your benefits: "))

# grosssalary = calc_gross(basic_salary,benefits)


# def area_triangle (a,b):
#     area = (a*b)/2
#     return area
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
# triangle1 = area_triangle(base,height)
# print(triangle1)


# def check_number (a):
#     if a % 2 ==0:
#         num = "Even"
#     else:
#         num = "Odd"
#     return num

# number = int(input("Enter number: "))
# nums = check_number(number)
# print(nums)


# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


def total_marks (math,eng,kis,sci,sis):
    total = math + eng + kis + sci + sis
    return total

math = int(input("Enter math: "))
eng = int(input("Enter eng: "))
kis = int(input("Enter kis: "))
sci = int(input("Enter sci: "))
sis = int(input("Enter sis: "))

marks=total_marks(math,eng,kis,sci,sis)
print(f"total marks: {marks}")

def average_marks(marks):
    average=marks/5
    return(average)

avg=average_marks(marks)
print(f"Average : {avg}")

def calc_grade (avg):
    if avg >79:
        grade = "A"
    elif avg <79 and avg >=60:
        grade = "B"
    elif avg <60 and avg >=49:
        grade = "C"
    elif avg <49 and avg >=40:
        grade = "D"
    else:
        grade ="E"
    return grade
    
score = calc_grade(avg)
print(f"grade: {score}")
