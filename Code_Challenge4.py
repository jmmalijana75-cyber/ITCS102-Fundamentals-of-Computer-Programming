# ACTIVITY 13 LOAN [CODE CHALLENGE 4 BETTER LOANING]
import getpass

username = "jmpogi"
password = "jmpogi123"

loguser = input("Username: --> ")
logpass = getpass.getpass("Password: --> ")


if loguser == username and logpass == password:
    firstname = input("What is your first name? --> ")
    jobdescript = input("What is your job? --> ")
    age = int(input("Enter your age --> "))
    is_employed = bool(input("Are you employed? (True/Leave it Blank) --> "))
    cred_score = eval(input("What is your credit score? (0-1000) --> "))
    annual_income = eval(input("What is your annual income? --> "))
    has_collateral = bool(input("Do you have any collateral? (True/Leave it blank) -->")) 

    if has_collateral == True:
        item_collateral = input("What item is your collateral? --> ")
        value_collateral = eval(input("How much value is your collateral? --> "))

        if value_collateral >= 30000:
            has_collateral = True
        else:
            has_collateral = False
    else:
        item_collateral = "None"

    if (age >= 21 and age <= 65) and is_employed == True:
        if cred_score >= 750:
            if annual_income >= 100000:
              i = 0.045
              inz = inz * 100
            else:
              i = 0.05
              inz = inz * 100
        elif 600 <= cred_score < 750:
            if has_collateral == True:
                i = 0.07
                inz = i * 100
            elif annual_income < 40000:
                i = 0.095
                inz = inz * 100
            elif has_collateral == True and annual_income < 40000:
                i = 0.080
                inz = inz * 100
            else:
                i = 0.08
                inz = i * 100
        else:
            print("Rejected: Credit score too low.")
            exit()
    else:
        print("Rejected: Fails baseline criteria.")
        exit()
        
    loan = eval(input("How much do you want to loan? --> "))
    print("First Name: ", firstname)
    print("Money loaned: ₱", loan)
    print("Interest: ", i, "%")
    print("Money Interest: ₱", loan * i)
    print("Loan with Interest: ₱", loan + (loan * i))
    print("Item Collateral: ", item_collateral)
    print("Value Collateral: ", value_collateral)
else:
    print("Account username/password is incorrect.")

