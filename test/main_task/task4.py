#Write a program which accepts email as form input or from terminal. Validate the email by checking 
#if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.

email =input("enter your email: ")
# if "@" in email and "." in email:
#     print("valid email address")
# else:
#     print("invalid email address format.")
if (email.startswith("@")) and (email.endswith(".")):
    print("valid email")
else:
    print("invalid email")