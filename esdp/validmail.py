import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Enter an email address: ")

if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
