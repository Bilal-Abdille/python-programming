#Continue with the same program and calculate an individual’s NHDF using:
 #i.e NHDF = gross_salary *  0.015



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


# calculating nssf based on 6% of gross salry with a mximum limit of 18000
nssf_percentage = 0.06
nssf = min(grossSalary * nssf_percentage,18000)   

# calculate nhdf based on 1.5% of gross salary
nhdf_percentage = 0.015
nhdf = grossSalary *nhdf_percentage   
#print(f"Gross salry: {grossSalary}" )
#print(f"NHIF contribution: {nhifContribution}")
#print(f"NSSF contribution: {nssf}")
print(f"NHDF contribution: {nhdf}")
        