# ATM system
    # 01) Display ATM functions
    #         Password check: 
    #             Balance
    #             Withdraw
    #             Deposit

print("{x}Welcome to kiriaththage pension eka{x}\n\n".format(x="*"*10))

# varibale define
pin = 1234
balance = 1000
error_message = "Try Again"

# get password from user (int value)
password = int(input("Enter your PIN : "))
if(password == pin):

    # option selection(balance or deposit or withdraw)
    print("Welcome kiriaththa\n1 - Balance\n2 - Deposit\n3 - Withdraw\n")

    option = int(input("Enter your option no : "))

    # balance
    if(option == 1): 
        print("Current Balance : {}".format(balance))

    # deposit    
    elif(option == 2):
        deposit = int(input("Enter amount : "))
        
        # deposit amount is in range rs.0 and rs.100,000
        if(0 <deposit <= 100000):
            print("deposit amount: {}\n".format(deposit))

            balance += deposit  #add deposit amount to deposit

            print("Current balance: {}\n".format(balance))

        elif(deposit > 100000): 
            print("Amount exceeded.", error_message)
        else:
            print("invalid input.", error_message)

    # withdraw
    elif(option == 3):
        withdraw = int(input("Enter amount : "))

        # withdraw amount is in range rs.0 and rs.100,000
        if(0 <withdraw <= balance):
            
            balance -= withdraw #reduce withdraw amout from current balace
            
            print("Withdraw amount : \n", withdraw)
            print("Current balance: \n", balance)            
        
        else: print("invalid input.", error_message)
else:
      print("Incorrect PIN.", error_message)

print("\n{x}Thank you{x}".format(x="*"*10))



