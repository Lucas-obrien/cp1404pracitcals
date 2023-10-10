"""
Emails
Estimate: 30 mins
Actual: 23:47
"""

name_to_email = {}

email_input = input("Email: ")
while email_input != "":
    email_details = email_input.split("@")
    name = ' '.join(email_details[0].split('.')).title()

    if input(f'Is your name {name}? (Y/n) ').upper() != "Y":
        name = input("Name: ")

    name_to_email[name] = email_input
    email_input = input("Email: ")
for name, email in name_to_email.items():
    print(f"{name} ({email})")

