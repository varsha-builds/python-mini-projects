dict = {
    "name" : "Varsha",
    "age" : 20,
    "city" : "Hyderabad"
}
user_input=input("Enter a key: ")
print(dict.get(user_input, "Not Found"))
