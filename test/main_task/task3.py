#Write a program which gets a phone number from a form input or terminal.
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01...
#Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”

phonenumber =int(input("enter your number: "))
valid =""
if (phonenumber[0:4]=="+254" and len(phonenumber)==13):
     valid= (f"the phone number is valid {phonenumber}")
elif((phonenumber[0:2]=="07" and len(phonenumber)==10) or (phonenumber[0:2]=="01" and len(phonenumber)==10)):
     
    new_phonenumber ="+254" + phonenumber[1:]
    valid=f"{new_phonenumber} is valid"
    print(valid)
elif((phonenumber[0:1]=="7" and len(phonenumber)==9) or (phonenumber[0:1]=="1" and len (phonenumber)==9)):
    new_phonenumber ="+254" + phonenumber
    valid = f"{new_phonenumber} is valid"
    print(valid)
elif(phonenumber[0:3]=="254" and len(phonenumber)==12):
    new_phonenumber= "+" + phonenumber
    valid = f" {new_phonenumber} is valid"
    print(valid)
else:
    print("in valid number")



# def validate_and_convert_phone_number(phone_number):
#     #checks if the phone number starts with the specified prefixes
#     if phone_number.startwith(("+254", "07", "71", "254", "01")):
#         #if it starts with "+254" or "01" then you add "+"
#         if phone_number.startwith(("254", "01")):
#             phone_number = "+" + phone_number
#           #if it starts with "07" or "71" add "+254"
#         elif phone_number.startwith(("07", "71")):
#             phone_number = "+254" + phone_number[1:]

#             return phone_number
#     else:
#             return "invalid phone number format"
# user_input = input("Enter a phone number: ")
# result = validate_and_convert_phone_number(user_input)
# print(result)