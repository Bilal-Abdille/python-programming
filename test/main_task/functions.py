# how to create functions

def calc_gross(benefits,basic_salary):
    gross_salary = basic_salary + benefits
    return gross_salary


basic_salary = float(input("enter your basic salary: "))
benefits = float(input("enter your benefits: "))

grosssalary = calc_gross(basic_salary,benefits)