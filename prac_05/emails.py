"""
Emails
Estimate: 30 mins
Actual:

"""

name_to_email = {}

email_input = "lucas.obrien@gmail.com" #input("Email: ")
email_detail = email_input.split("@")
# name = email_detail[0].split(".")

name = ' '.join(email_detail[0].split('.')).title()



