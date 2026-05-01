def change_pin():
    while True:
        account_num=input("Enter your account number: ")
        if len(account_num)==10:
            print("check OTP on your registered phone number.")
            otp=input("please enter 4 digits otp: ")
            if len(otp)==4:
                break
            else:
                print("Enter valid otp.")
        else:
            print("Please enter valid account number.")
    while True:
        current_pin=input("Please enter your current pin:")
        new_pin=int(input("Please enter your new pin:"))
        confirm_pin=int(input("Please re-enter your new pin:"))
        if new_pin !=confirm_pin:
            print("new_pin and confirm_pin does't match.")
            print("Please try again.")
        else: 
            print('''Processing......
Pin set successfully
Take your card''')
            break