# Write a program that takes the email and password as input from a user and checks if they are equal to
# “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print
# “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.


correct_email = "admin@mail.com"
correct_password = "Admin@123"

# Initialize the number of attempts
attempts = 0

# Give the user three attempts
while attempts < 3:
    # Get email and password from user input
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    # Check if email and password are correct
    if email_input == correct_email and password_input == correct_password:
        print("Login is Successful.")
        break
    else:
        print("Invalid username or password. Try again.")
        attempts += 1

# Check if the user is blocked
if attempts == 3:
    print("You have been blocked. Too many unsuccessful attempts.")
