password = input("Enter Your Password: ")
password_length = len(password)
if password_length > 0 and password_length < 8:
    print("Weak Password")
elif password_length >= 8 and '@' in password:
    print("Strong Password")
else:
    print("Medium Password")