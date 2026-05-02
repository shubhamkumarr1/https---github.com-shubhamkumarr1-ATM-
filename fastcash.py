def fast_cash(balance, create_pin):
    while True:
        pin = int(input("Please enter your pin: "))
        
        if pin == create_pin:
            amount = int(input("Please enter the amount you can withdraw: "))
            
            if amount % 100 != 0:
                print("Please enter valid amount.")
                continue
            
            print("your transaction is being processed.....")
            print("Transaction completed.")
            print("Take your card.")
            print("Thank you for using our ATM. Have a nice day!")
            return         
        else:
            print("Please enter valid pin")