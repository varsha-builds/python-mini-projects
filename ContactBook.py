contacts = {
    "Sam" : "9876543210",
    "Alex" : "9123456780",
    "John" : "9988776655"
}
user_input = (input("Enter Contact Name: "))
user_input1 = user_input.title()
print(contacts.get(user_input1,"Contact Not Found"))
