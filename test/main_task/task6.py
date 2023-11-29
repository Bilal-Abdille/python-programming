correct_password = "admin@123"
attempts = 0

#give the user 4 attempts
while attempts<4:
    user_password = input("Enter the password: ")

    #check if the password is correct
    if user_password==correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
        attempts+=1

        #check if the account is blocked
if attempts ==4:
    print("Account blocked. Too many incorrect attempts.")