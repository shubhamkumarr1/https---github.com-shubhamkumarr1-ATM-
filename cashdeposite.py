def deposite(balance,create_pin):
    while True:
        pin =int(input("Please enter your pin: "))
        if pin==create_pin:
            while True:
                account = input("Enter account type (saving/current): ").lower()
                if account not in ["saving", "current"]:
                    print("Invalid account type")
                    continue 
                print("Deposite per transaction limite:100000")
                # amount1=balance
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
                            print("total remaing amount:",balance)
                        another_withdrawal=str(input("Do you want to perform another transaction? (yes or no): "))
                        if another_withdrawal=="yes":  
                            continue
                        else:
                            print("Thank you for using our ATM. Have a nice day!")
                            return balance    
                    else:
                        print("Invalid amount, please enter a multiple of 100")
        else:
            print("Please enter valid pin")                 