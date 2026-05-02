from fastcash import fast_cash
from withdrawal import cashwithdrawal
from languages import languages
from cashdeposite import deposite
from pinchange import change_pin
from transfer import transfer
from Balanceinquiry import balance_enquiry
username=""
create_pin=0
balance=0

while True:
    print("**===========||___WELCOME___||===========**")
    print("Please insert your card")
    print("Hi,please do not remove your chip card.")
    print("leave your card inserted during the entire transaction")
    print("choose language")
    print("1:English")
    print("2:Hindi")
    print("3:Punjabi")
    print("4:Bengoli")
    print("5:exit")
    choose= int(input("Enter the number corresponding to your language: "))
    languages(choose) 
    if choose==5: 
        break
    while True:
        print("PRESS 1: REGISTRATION/Creation ATM PIN")
        print("PRESS 2: LOGIN to Using the ATM")
        choice=int(input("Please select the option."))
        if choice==1:
            print("-------REGISTRATION/SIGNUP-------")
            username=input("USERNAME:") 
            create_pin=int(input("CREATE PIN:"))  
            balance=int(input("INITIAL AMOUNT:"))  
            print("*****SIGNUP SUCCESSFULLY*****") 
            print("Now Please Login To Continue")
        elif choice==2:
            print("*****LOGIN*****")
            user=input("Enter username:")
            if username==user:
                pin=int(input("Enter pin:"))
                if pin==create_pin:
                    print("*****LOGIN SUCCESSFULLY*****")
                    print("select your transaction")
                    print("1:Cash Withdrawal")
                    print("2:Deposit")
                    print("3:Pin change")
                    print("4:Fast cash")  
                    print("5:Transfer")
                    print("6:Balance enquiry")
                    transaction=int(input("Enter the number corresponding to your transaction: "))
                    if transaction==1: 
                        balance=cashwithdrawal(balance, create_pin)
                        break
                    elif transaction==2:  
                        balance=deposite(balance, create_pin)
                        break
                    elif transaction==3:  
                        create_pin=change_pin(create_pin) 
                        break
                    elif transaction==4:  
                        balance=fast_cash(balance)
                        break
                    elif transaction==5:  
                        balance=transfer(balance)
                        break
                    elif transaction==6:  
                        balance_enquiry(balance)
                        break
                    else:
                        print("Invalid input, please try again.")
                # else:
                #     print("Incorrect pin")  
            else:
                print("uswer not found")    
        else:
            print("invalid choice.") 
    