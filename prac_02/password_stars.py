"""
function main
    password = get valid password
    print asterisks

function print stars
    print asterisks equal to length of word

function get valid password
    get password
    if password is less than minimum length
        display invalid password
        get password
    return password
"""

MINIMUM_PASSWORD_LENGTH = 5


def main():
    """Has the user input a password, then prints an amount of * equal to the length of the password."""
    password = get_password()
    print_stars(password)


def print_stars(word):
    """Print * equal to the length of string passed in."""
    print("*" * len(word))


def get_password():
    """Gets a password, then checks if the password meets a minimum length, then returns password if valid"""
    password = input("Enter a password: ")
    if len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password too short")
        password = input("Enter a password: ")
    return password


main()
