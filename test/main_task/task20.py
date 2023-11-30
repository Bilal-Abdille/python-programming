# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

basicSalary = float(input("Enter your basic salary (Kshs):"))
benefits = float(input("Enter your benefits (Kshs):"))


#calculate gross salary

grossSalary = basicSalary + benefits

#determing nhif based on gross salary
if (grossSalary <= 5999):
        nhifContribution = 150
elif(grossSalary <= 7999):
        nhifContribution = 300
elif(grossSalary <= 11999):
        nhifContribution = 400
elif(grossSalary <= 14999): 
        nhifContribution = 500
elif(grossSalary <= 19999):
        nhifContribution = 600
elif(grossSalary <= 24999):
        nhifContribution = 750
elif(grossSalary <= 29999):
        nhifContribution = 850
elif(grossSalary <= 34999):
        nhifContribution = 900
elif(grossSalary <= 39999):
        nhifContribution = 950
elif(grossSalary <= 44999):
        nhifContribution = 1000
elif(grossSalary <= 49999):
        nhifContribution = 1100
elif(grossSalary <= 59999):
            nhifContribution = 1200
elif(grossSalary <= 69999):
            nhifContribution = 1300
elif(grossSalary <= 79999):
            nhifContribution = 1400
elif(grossSalary <= 89999):
            nhifContribution = 1500
elif(grossSalary <= 99999):
        nhifContribution = 1600
else:
       nhifContribution = 1700

# nhdf below
# calculate nhdf based on 1.5% of gross salary
nhdf_percentage = 0.015
nhdf = grossSalary *nhdf_percentage  

#nssf below
# calculating nssf based on 6% of gross salry with a mximum limit of 18000
rate = 0.06
if grossSalary >0 and grossSalary <=18000:
    nssf = grossSalary*rate
else:
    nssf = 18000*rate
      
# payee below
nhdf_percentage = 0.015
nhdf = grossSalary *nhdf_percentage 

taxable_income = grossSalary-(nssf + nhdf)
relief = 2400
if taxable_income<=24000:
    payee = (taxable_income *0.1)-relief
elif(taxable_income>24000 and taxable_income <=32333):
    payee = ((24000*0.1)+ ((taxable_income-24000)*0.25))-relief
else:
    payee = ((24000*0.1)+(8333*0.25)+ ((taxable_income-32333)*0.3))-relief

netsalary = grossSalary-(nhifContribution + nhdf + nssf + payee)


print(f"nhdf: {nhdf}")
print(f"nssf: {nssf}")
print(f"taxableincome: {taxable_income}")
print(f"payee: {payee}")
print(f"nhif: {nhifContribution}")
print(f"Net salary: {netsalary}")

        


