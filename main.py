from fastcash import fast_cash
from withdrawal import withdrawal
from languages import languages
from cashdeposite import deposite
from pinchange import change_pin
from transfer import transfer
from Balanceinquiry import balance_enquiry
while True:
    print("WELCOME !")
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
    print("select your transaction")
    print("1:Cash Withdrawal")
    print("2:Deposit")
    print("3:Pin change")
    print("4:Fast cash")
    print("5:Transfer")
    print("6:Balance enquiry")
    transaction=int(input("Enter the number corresponding to your transaction: "))
    if transaction==1:  withdrawal()
    elif transaction==2:  deposite()
    elif transaction==3:  change_pin() 
    elif transaction==4:  fast_cash()
    elif transaction==5:  transfer()
    elif transaction==6:  balance_enquiry()
    else:
        print("Invalid input, please try again.")