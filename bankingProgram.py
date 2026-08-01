def show_balance(balance):
    print ("----------------------------")
    print (f"You balance is ${balance:.2f}")
    print ("----------------------------")

def deposit():
    print ("----------------------------")
    amount = float(input ("Enter an amount to be deposited: "))
    print ("----------------------------")

    if (amount < 0):
        print ("----------------------------")
        print ("Thiis is not a valid amount")
        print ("----------------------------")
        return 0
    else:
        return amount

def withdraw(balance):
    print ("----------------------------")
    amount = input ("Enter amount to be withdrawn: ")
    print ("----------------------------")

    if (amount > balance):
        print ("----------------------------")
        print ("Insufficient funds")
        print ("----------------------------")
        return 0 
    
    elif (amount < 0):
        print ("----------------------------")
        print ("Amount must be greater than zero")
        print ("----------------------------")
        return 0 
    
    else :
        return amount 

def main():
    balance = 0
    isRunning = True

    while isRunning:
        print ("----------------------------")
        print ("      Banking program")
        print ("----------------------------")
        print ("1. Show balance")
        print ("2. Deposit")
        print ("3. Withdraw")
        print ("4. Exit")

        choice = input ("Enter your choice (1-4): ")

        if (choice == "1"):
            show_balance(balance)

        elif (choice == "2"):
            balance += deposit()

        elif (choice == "3"):
            balance -= withdraw(balance)

        elif (choice == "4"):
            isRunning = False

        else :
            print ("----------------------------")
            print ("Not a valid choice")
            print ("----------------------------")

    print ("----------------------------")
    print ("Thankyou! Have a nice day!")
    print ("----------------------------")

if __name__ == '__main__':
    main()

