def add(first_number, second_number):
    return first_number+second_number
def subtract(first_number, second_number):
    return first_number-second_number
def  multiply(first_number, second_number):
    return first_number*second_number 
def divide(first_number, second_number):
    return first_number/second_number
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
operation = input("Choose Operation (+,_,*,/): ")
if operation == '+':
    print(add(first_number, second_number))
elif operation == '-':
    print(subtract(first_number, second_number))
elif operation == '*':
    print(multiply(first_number, second_number))
elif operation == '/':
    print(divide(first_number, second_number))
else:
    print("Invalid Operation")
        