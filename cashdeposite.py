from balace_amount import total_amount 
def deposite():
    while True:
        pin = input("Please enter your 4-digit pin: ")
        if len(pin) < 4 or len(pin) > 4:
            print("Invalid pin")
        else:
            break 
    account=input("Please select your account type:(saving or current) ")
    print("Deposite per transaction limite:100000")
    balance=total_amount
    while True: 
        print("Acceptable denomination Rs 100, Rs 200, Rs 500.")
        amount=int(input("Please insert your case"))
        if amount > 100000:
            print("Deposit limit exceeded")
        elif amount%100==0:
            balance+=amount
            print('''Please wait...Validating cash...
your cash is varified.
Your transaction is being processess please wait.....
Transaction completed.''')
            str3=str(input("You want check the balance in your account:(yes/no) ")).lower()
            if str3=="yes":
                # show_balance=total_amount+amount
                print("total remaing amount:",balance)
            another_withdrawal=str(input("Do you want to perform another transaction? (yes or no): "))
            if another_withdrawal=="yes":  
                continue
            else:
                print("Thank you for using our ATM. Have a nice day!")
                break    
        else:
            print("Invalid amount, please enter a multiple of 100")