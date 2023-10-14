"""
Emails
Estimate: 30 mins
Actual: 23:47
"""

name_to_email = {}


email = input("Email: ")
while email != "":
    name = ' '.join((email.split('@'))[0].split('.')).title()
    choice = input(f'Is your name {name}? (Y/n) ').upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")

for name, email in name_to_email.items():
    print(f"{name} ({email})")
