from balace_amount import total_amount
def balance_enquiry():
    pin = int(input("Please enter your pin: ")) 
    account_type = input("Type of account (saving/current/loan): ")
    show_balance = input("Do you want to display the balance on screen? (yes/no): ")
    if show_balance.lower() == "yes":
        print("Available balance in your account:", total_amount)
    feedback = input("How was your overall experience with bank name (like SBI, BOI): ")
    print("Transaction completed.")
    print("Take your card.")