def calc_gross(benefits,basic_salary):
     gross_salary = basic_salary + benefits
     return gross_salary


basic_salary = float(input("enter your basic salary: "))
benefits = float(input("enter your benefits: "))

Grosssalary =calc_gross(benefits,basic_salary)
print(f"grosssalary: {Grosssalary}")

#nhif functions
def calc_nhif(a):
     
        if (a <= 5999):
                nhifContribution = 150
        elif(a <= 7999):
                nhifContribution = 300
        elif(a <= 11999):
                nhifContribution = 400
        elif(a <= 14999): 
                nhifContribution = 500
        elif(a <= 19999):
                nhifContribution = 600
        elif(a <= 24999):
                nhifContribution = 750
        elif(a <= 29999):
                nhifContribution = 850
        elif(a <= 34999):
                nhifContribution = 900
        elif(a <= 39999):
                nhifContribution = 950
        elif(a <= 44999):
                nhifContribution = 1000
        elif(a <= 49999):
                nhifContribution = 1100
        elif(a <= 59999):
                nhifContribution = 1200
        elif(a <= 69999):
                nhifContribution = 1300
        elif(a <= 79999):
                nhifContribution = 1400
        elif(a <= 89999):
                nhifContribution = 1500
        elif(a <= 99999):
                nhifContribution = 1600
        else:
                nhifContribution = 1700
        return nhifContribution

NHIF = calc_nhif(Grosssalary)
print(f"nhif: {NHIF}")


#nssf functions
def calc_nssf (gross_salary,rate = 0.06):
        if gross_salary >0 and gross_salary <=18000:
             nssf = gross_salary*rate
        else:
             nssf = 18000*rate
        return nssf

NSSF = calc_nssf(Grosssalary )
print(f"nssf: {NSSF}")

#nhdf functons
def calc_nhdf (gross_salary,rate = 0.015):
        nhdf = gross_salary * rate
        return nhdf

NHDF = calc_nhdf(Grosssalary)
print(f"nhdf: {NHDF}")

#taxable_income functons
def calc_taxable_income(gross_salary,NSSF,NHDF):
        taxableincome = gross_salary - (NSSF + NHDF)
        return taxableincome


Taxableincome = calc_taxable_income(Grosssalary,NSSF,NHDF)
print(f"taxableincome: {Taxableincome}")

#payee functions
def calc_payee(taxableincome):
        if taxableincome<=24000:
               grosspayee = (taxableincome *0.1)-2400
        elif(taxableincome > 24000 and taxableincome <= 32333):
               grosspayee =((24000*0.1)+ ((taxableincome-24000)*0.25))-2400
        else:
               grosspayee = ((24000*0.1)+(8333*0.25)+((taxableincome-32333)*0.3))-2400

               return grosspayee
        
        
        
PAYEE = calc_payee(Grosssalary)
print(f"payee: {PAYEE}")

#net salary functions

def calc_netsalary(Grosssalary,NHIF,NHDF,NSSF,PAYEE):
       netsalary = Grosssalary-(NHIF+NHDF+NSSF+PAYEE)
       return netsalary

Netsalary = calc_netsalary(Grosssalary,NHIF,NHDF,NSSF,PAYEE)
print(f"NET SALARY: {Netsalary}")