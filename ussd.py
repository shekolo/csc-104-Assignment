import random
def transac_option():
    print("1.Check you balance\n2.Transfer\n3.Airtime\n4.Transaction history")
    transaction_option = str(input("Please select an option: "))
    if(transaction_option == '1'):
        balance = random.randint(33346, 88792)
        print("Your account balance is "+balance+" naira ")
        exit_code = input("ENTER 1 TO RETURN TO MENU\nENTER 2 TO END")
        if(exit_code == 1):
             transaction_option = int(input("Please select an option: "))
    elif(transaction_option == '2'):
        acct_no = input("Enter account you want  to Transfer money to: ")
        amount = input("Enter amount: ")
        pin = input("Enter 4 didgit pin: ")
        print("Do you want to send "+str(amount)+" to this account number "+str(acct_no)+"?")
        print("1. YES\n2. NO")
        opt = input("Enter 1 or 2: ")
        if(opt == 1):
            print("TRANSACTION SUCCESSFUL")
            print("ENTER 1 TO RETURN T0 MENU")
            print("ENTER 2 TO END")
        elif(opt == 2):
            transac_option()
        else:
            print("")
    elif(transaction_option == '3'):
        print("1. For self")
        print("2. For others")
        x = input("Enter 1 or 2: ")
        if(x  == 2):
            amount = input("Enter amount: ")
            airtime_number = input("Enter amount you want to buy airtime for: ")
            print("Do you want to buy "+str(amount)+" naira worth of airtime for "+str(airtime_number)+"?")
            print("1. YES")
            print("2. NO")
            selected = input("Enter 1 or 2: ")
            if(selected == 1):
                print("TRANSACTION SUCCESSFUL")
                print("ENTER 1 TO RETURN TO MENU")
                print("ENTER 2 TO END")
                exit_option = input("Enter 1 or 2: ")
                if(exit_option == 1):
                    transac_option()
                elif(exit_option == 2):
                    print("Thanks for banking with us!")
                else:
                    print("Please choose a valid option")
    elif(transaction_option == '4'):
        print("An SMS message will be sent to you shortly.")
    
def transaction_options():
    print("1.Check you balance\n2.Transfer\n3.Airtime\n4.Transaction history")
    transaction_option = str(input("Please select an option: "))
    if(transaction_option == '1'):
        balance = 33346
        print("Your account balance is "+str(balance)+" naira ")
        exit_code = str(input("ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: "))
        if(exit_code == '1'):
             transaction_option = str(input("Please select an option: "))
    elif(transaction_option == '2'):
        acct_no = input("Enter account you want  to Transfer money to: ")
        amount = input("Enter amount: ")
        pin = input("Enter 4 didgit pin: ")
        print("Do you want to send "+str(amount)+" to this account number "+str(acct_no)+"?")
        print("1. YES\n2. NO")
        success_option = str(input("Enter 1 or 2: "))
        if(success_option == '1'):
            print("TRANSACTION SUCCESSFUL")
            print("ENTER 1 TO RETURN T0 MENU")
            print("ENTER 2 TO END")
            y = str(input("Enter 1 or 2"))
            if(success_option == '1'):
                transac_option()
    elif(transaction_option == '3'):
        print("1. For self")
        print("2. For others")
        airtime_opt = str(input("Enter 1 or 2: "))
        if(airtime_opt  == '2'):
            amount = input("Enter amount: ")
            airtime_number = input("Enter amount you want to buy airtime for: ")
            print("Do you want to buy "+str(amount)+" naira worth of airtime for "+str(airtime_number)+"?")
            print("1. YES")
            print("2. NO")
            selected = str(input("Enter 1 or 2: "))
            if(selected == '1'):
                print("TRANSACTION SUCCESSFUL")
                print("ENTER 1 TO RETURN TO MENU")
                print("ENTER 2 TO END")
                exit_option = str(input("Enter 1 or 2: "))
                if(exit_option == '1'):
                    transac_option()
                elif(exit_option == '2'):
                    print("Thanks for banking with us!")
    elif(transaction_option == '4'):
        print("An SMS message will be sent to you shortly.")
def info():
    print("Here are the available bank ussd codes: ")
    print("Access: *901#")
    print("UBA: *919#")
    print("FCMB: *3291#")
    print("Polaris (skye): *833#")
    print("GTBank: *737#")
    print("Zenith: *966#")
    print("Ecobank: *326#")
    print("First Bank: *894#")
    print("Stanbic IBTC Bank: *909")
    print("Diamond Bank: *426#")
    print("Fidelity Bank: *770#")
    print("Sterling Bank: *822#")
    print("Unity Bank: *7799#")
    
info()
def ussd():
    user_selected_bank = int(input("please type in your bank ussd code: "))
    if(user_selected_bank):
        if(user_selected_bank == 901):
            print("You have entered the code for Access: *901#")
            transaction_options()
        elif(user_selected_bank == 919):
             print("You have entered the code for UBA: *919#")
             transaction_options()
        elif(user_selected_bank == 329):
             print("You have entered the code for FCMB: *3291#")
             transaction_options()
        elif(user_selected_bank == 833):
             print("You have entered the code for polarise (skye): *833#")
             transaction_options()
        elif(user_selected_bank == 737):
             print("You have entered the code for GTBank: *737#")
             transaction_options()
        elif(user_selected_bank == 966):
             print("You have entered the code for Zenith: *966#")
             transaction_options()
        elif(user_selected_bank == 326):
             print("You have entered the code for Ecobank: *326#")
             transaction_options()
        elif(user_selected_bank == 894):
             print("You have entered the code for First Bank: *894#")
             transaction_options()
        elif(user_selected_bank == 909):
             print("You have entered the code for Stanbic IBTC Bank: *909#")
             transaction_options()
        elif(user_selected_bank == 426):
             print("You have entered the code for Diamond: *426#")
             transaction_options()
        elif(user_selected_bank == 770):
             print("You have entered the code for Fidelity Bank: *770#")
             transaction_options()
        elif(user_selected_bank == 822):
             print("You have entered the code for Sterling Bank: *822#")
             transaction_options()
        elif(user_selected_bank == 7799):
             print("You have entered the code for Unity Bank: *7799#")
             transaction_options()
        else:
            print("Invalid bank ussd code")
            ussd()
    else:
        print("")
ussd()