account_balance = 1000.0
withdrawal_amount = float(input("Enter Withdrawal Amount: "))
remaining_balance = account_balance - withdrawal_amount
if withdrawal_amount <= account_balance:
    print("Amount Deducted")
    print("Withdrawal Successful")
    print("Remaining Amount", remaining_balance)
else:
    print("Insufficient Balance")
    
