secret_number = "7"
user_attempt = 0
while user_attempt < 3:
    user_input = input("Enter Your Guess: ")
    if user_input == secret_number:
        print("You Won!")
        break
    else: 
        print("Try Again")
        user_attempt += 1
    if user_attempt == 3 and user_input != secret_number:
        print("You Lost")

