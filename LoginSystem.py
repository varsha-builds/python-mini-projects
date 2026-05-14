Username = 'Varsha'
Password = 'Varsha@123'
username = input("Enter the Username: ")
password = input("Enter the Password: ")
if Username == username and Password == password:
    print("Login Successful")
elif Username != username and Password == password:
    print("Invalid Username")
elif Username == username and Password != password: 
    print("Invalid Password")
else: 
    print("Login Failed")

