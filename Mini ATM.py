create_pin=int(input("Create pin numer:"))
balance=250000

pin=int(input("Enter pin numer:"))

while pin != create_pin:
    print("\nIncorrect pin, try again",)
    pin=int(input("\nEnter pin num:"))

print("\nLogin successful")

while True:   
    print("\n1.Check balance  2.Deposite money")
    print("3.Withdraw money 4.Exit")
    inputs=int(input("\nEnter value of your task:"))
    
    if inputs==1:      
        print("\nYour balance",balance)        
              
    elif inputs==2:
        deposite=int(input("Enter amount to deposite:"))
        if deposite>0:
            balance = deposite + balance
            print("\nYour amount deposited!",balance)
        else:
            print("\nEnter positive amount")
                
    elif inputs==3:
        withdraw=int(input("Enter amount to withdraw:"))   
        if withdraw>balance:
            print("\nInsuficient balance")
        else:
            balance = balance - withdraw
            print("\nYour amount withdrawn! \nBalance:",balance)
            
    elif inputs ==4:
         print("\nTranscation completed, session ended.")
         print("\nThank you for choosing our bank!")
         break
    else:
        print("Enter the valid input and try again")
        
