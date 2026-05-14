age=int(input("Enter Your Age: "))
if age >= 0 and age < 18:
    print("Minor")
elif age >= 18 and age <= 59: 
    print("Adult")
else: 
    print("Senior")
