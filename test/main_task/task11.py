# Write a program that takes the date of birth of a person and 
# the program outputs the age in terms of years,months,days TODAYf
from datetime import datetime
def find_age(today=None,dob=None,):
        today = datetime.now()
        dob = input("Enter DOB (dd-mm-yyyy): ")
        sdob = dob.split("-")

        if len(sdob) != 3 or int(sdob[0]) > 31 or int(sdob[1]) > 12 or int(sdob[2]) < 1900 or int(sdob[2]) > today.year:
           result = "Wrong date format"
        else:
         dob_date = datetime(day=int(sdob[0]), month=int(sdob[1]), year=int(sdob[2]))
         age = today - dob_date
         years = age.days // 365
         months = (age.days % 365) // 31
         days = (age.days % 365) % 31

        result = f"{years} years {months} months {days} days"

        return result

value = find_age()
print(value)