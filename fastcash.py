def fast_cash():
    pin=(input("Please enter your pin: "))
    while True:
        if len(pin) < 4 or len(pin) > 4:
            print("Invalid pin")
            pin = input("Please enter your 4-digit pin: ")
        else:
            break
    amount=int(input("Please enter the amount you can withdraw: "))
    if amount%100!=0:
        print("Please enter valid amount. ")
    else:
        print("your transaction is being processess.....")
        print("Transaction completed.")
        print("Take your card.")
        print("Thank you for using our ATM. Have a nice day!")