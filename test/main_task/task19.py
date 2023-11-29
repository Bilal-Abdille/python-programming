# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using


basicSalary = float(input("Enter your basic salary (Kshs):"))
benefits = float(input("Enter your benefits (Kshs):"))

#calculate gross salary

grossSalary = basicSalary + benefits

  #nssf below
rate = 0.06
if grossSalary >0 and grossSalary <=18000:
    nssf = grossSalary*rate
else:
    nssf = 18000*rate

    #nhdf

    #  calculate nhdf based on 1.5% of gross salary
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

  
      
    
#print(nssf)

# nhdf = grossSalary*0.015


print(f"PAYEE: {payee}")