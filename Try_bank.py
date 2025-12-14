def show_balance():
    
    print(f" Your balance is $ {balance: .2f}")

    #print("input")

def deposit():

    amount = float(input("Enter your amount to be deposited :  "))

    if amount < 0:
        print("That's not a valid amount ")
        return 0
    else:
        return amount

def withdraw():

    amount=float(input ("Enter your amout you withdrawn : "))

    if amount > balance :
        print("Sorry you have insufficient amount")
        return 0
    elif amount < 0:
        print ("Amount must be greater then 0 ")
    else:

        return amount

###def main():

    balance=0
is_running = True

while is_running:
    print("••••••••••••••••••••••••••")
    print("Banking Program")
    print("1. Show balance ")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit" )
    print("••••••••••••••••••••••••••")

    choice= input ("Enter your choice  (1- 4 : )" )
    
    if choice == "1":
        print()
        show_balance()
        print()
    elif choice == "2":
        balance +=deposit()
    elif choice =="3":
        balance -=withdraw()
    elif choice =="4":
        is_running = False 
    else :
        print ("That is not a valid choice")

    print("Thank you Have a Nice Day")

#if __name__== '__main__':
#main()



