# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 

basicSalary = float(input("Enter your basic salary (Kshs):"))
benefits = float(input("Enter your benefits (Kshs):"))

#calculate gross salary

grossSalary = basicSalary + benefits

rate = 0.06
if grossSalary >0 and grossSalary <=18000:
    nssf = grossSalary*rate
else:
    nssf = 18000*rate
    
#print(nssf)

nhdf = grossSalary*0.015

taxable_income = grossSalary-(nssf + nhdf)
print(f"NHDF: {nhdf}")


# taxable_income = gross salary - (NSSF + NHDF) 
print(f"Gross salry: {grossSalary}" )
# print(f"NHIF contribution: {nhifContribution}")
# print(f"NSSF contribution: {nssf}")
# print(f"NHDF contribution: {nhdf}")
print(f"Taxableincome: {taxable_income}")
        