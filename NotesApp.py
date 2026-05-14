notes = input("Enter Your Notes: ")
with open("notes.txt", "a") as file:
    file.write(notes + "\n")
    print("Note Saved Successfully")
with open("notes.txt", "r") as file:
    print(file.read())

 
