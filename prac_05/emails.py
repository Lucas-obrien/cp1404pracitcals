"""
Emails
Estimate: 30 mins
Actual: 23:47
"""

name_to_email = {}

email = input("Email: ")
while email != "":
    email = email.split("@")
    name = ' '.join(email[0].split('.')).title()
    if input(f'Is your name {name}? (Y/n) ').upper() != "Y":
        name = input("Name: ")
    name_to_email[name] = "@".join(email)
    email = input("Email: ")

for name, email in name_to_email.items():
    print(f"{name} ({email})")

