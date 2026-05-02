def cashwithdrawal(balance,create_pin):
    while True:
        pin =int(input("Please enter your pin: "))
        if pin==create_pin:
            while True:
                account = input("Enter account type (saving/current): ").lower()
                if account not in ["saving", "current"]:
                    print("Invalid account type")
                    continue
                amount=int(input("Please enter the amount you want to withdraw: "))
                if balance<amount:
                    print("Insufficient balanace")
                    print("Try again")
                elif amount%100==0:

                    print("Your transaction is being processess please wait.....")
                    print("Please collect your cash")
                    str3=str(input("You want check the balance in your account:(yes/no) ")).lower()
                    if str3=="yes":
                        balance-=amount
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
        break  
        