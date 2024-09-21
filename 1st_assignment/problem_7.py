'''Problem 7: Password Validator
Create a program that checks whether a password entered by the user is valid based on the
following rules:
• The password must be at least 8 characters long.
• The password must contain at least one number and one uppercase letter'''

# Get input from the user
password = input("Enter a password: ")

# Check if the password is at least 8 characters long, contains a number and an uppercase letter
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Password is valid.")
else:
    print("Password must be at least 8 characters long and contain at least one number and one uppercase letter.")
