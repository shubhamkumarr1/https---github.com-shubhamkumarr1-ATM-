from balace_amount import total_amount 
def withdrawal():
    pin =input("Please enter your pin: ")
    while True:
        if len(pin) < 4 or len(pin) > 4:
            print("Invalid pin")
            pin = input("Please enter your 4-digit pin: ")
        else:
            break 
    account=(input("Please select your account type:(saving or current) "))
    while True:
        amount=int(input("Please enter the amount you want to withdraw: "))
        if total_amount<amount:
            print("Insufficient balanace")
            print("Try again")
        elif amount%100==0:
            print("Your transaction is being processess please wait.....")
            print("Please collect your cash")
            str3=str(input("You want check the balance in your account:(yes/no) ")).lower()
            if str3=="yes":
                show_balance=total_amount-amount
                print("total remaing amount:",show_balance)
            another_withdrawal=str(input("Do you want to perform another transaction? (yes or no): "))
            if another_withdrawal=="yes":  
                continue
            else:
                print("Thank you for using our ATM. Have a nice day!")
                break
        else:
            print("Invalid amount, please enter a multiple of 100")
           