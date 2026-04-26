def deposite():
    pin=int(input("Please enter your pin:"))
    account=str(input("Please select your account type:(saving or current) "))
    print("DEPOSITE PER TRANSACTION LIMITE:100000")
    while True:
        print("Acceptable denomination Rs 100, Rs 200, Rs 500.")
        amount=int(input("Please insert your case"))
        if amount%100==0:
            print('''Please wait...Validating cash...
your cash is varified.
Your transaction is being processess please wait.....
Transaction completed.
Take your card.
Thank you for using our ATM. Have a nice day!''')
            break
        else:
            print("Invalid amount, please enter a multiple of 100")