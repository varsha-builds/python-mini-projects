price = float(input("Enter Item Price: "))
quantity = float(input("Enter the Quantity: "))
total =  price*quantity
if total >= 500:
    print("Apply Discount")
    discount = total * 10/100 
    print(discount)
else:
    print("No Discount")
    discount = 0.0
    print(discount)
original_total = total
final_total = total - discount
print("Original Total" , original_total)
print("Final Total", final_total)
