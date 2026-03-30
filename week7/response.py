import validators

email = input("Email: ")
if validators.email(email):
    print("Valid")
else:
    print("Invalid")