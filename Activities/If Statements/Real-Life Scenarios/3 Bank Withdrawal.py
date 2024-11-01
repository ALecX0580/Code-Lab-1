account_balance = float(input("Enter account balance: "))
withdraw_account = float(input("Enter the amount you want to witdraw: "))

if withdraw_account <= account_balance:
    new_balance = account_balance - withdraw_account
    print(f"Withdrawal succesful. Your new balance is: £{new_balance}")
    if  new_balance > 1000:
        print("\033[1mHello esteemed client!\033[0m")
    elif new_balance < 100:
        print(f"Warning: Your £{new_balance} is below £100.")
else:
    print(f"Insufficient funds. Withdrawal not allowed.")