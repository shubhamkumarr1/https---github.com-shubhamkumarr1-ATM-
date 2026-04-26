def change_pin():
    account_num=int(input("Enter your accounrt number: "))
    print("check OTP on your registered phone number.")
    otp=int(input("please enter 4 digits otp: "))
    while True:
        current_pin=int(input("Please enter your current pin:"))
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