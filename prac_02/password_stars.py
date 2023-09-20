"""write a program that asks the user for a password, with error-checking to repeat if the password doesn't
 meet a minimum length set by a variable."""

MINIMUM_PASSWORD_LENGTH = 5

password = input("Enter a password: ")

if len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password too short")
    password = input("Enter a password: ")

print("*" * len(password))
