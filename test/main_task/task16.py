# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

basicSalary = float(input("Enter your basic salary (Kshs):"))
benefits = float(input("Enter your benefits (Kshs):"))

#calculate gross salary

grossSalary = basicSalary + benefits

# calculating nssf based on 6% of gross salry with a mximum limit of 18000
rate = 0.06
if grossSalary >0 and grossSalary <=18000:
    nssf = grossSalary*rate
else:
    nssf = 18000*rate
      

print(f"NSSF contribution: {nssf}")
        







