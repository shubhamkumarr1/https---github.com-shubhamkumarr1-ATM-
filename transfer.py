def transfer():
    print("Account based transfer")
    pin=int(input("Please enter your pin:"))
    account_type=str(input("type of account(like saving,current,loan)"))
    while True:
        account_num=int(input("Enter the account number of the recipient: "))
        confirm_account_num=int(input("Please re-enter the account number of the recipient: "))
        if account_num !=confirm_account_num:
            print("Account number and confirm account number does't match.")
            print("Please try again.")
        else:
            amount=int(input("Enter the amount you want to transfer: "))
            if amount%100!=0:
                print("Please enter valid amount. ")
            else:
                print("your transaction is being processess.....")
                print("Transaction completed.")
                print("Take your card.")
                print("Thank you for using our ATM. Have a nice day!")
                break