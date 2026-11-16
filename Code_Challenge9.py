print("Task 1")

amount = float(input("Enter the Amount Loan:$"))
year = int(input("Enter the Year Loan Period:"))

months = year * 12
rate = 0.03
principal = amount/months
remaining = amount

print("\nPayment Schedule")
print("Month | Payment | Interest | Principal | Reamining Balance")

for month in range(1, months + 1):

    interest = remaining * rate / 12 
    payment = principal + interest
    remaining = remaining - principal

    if month == months:
        remaining = 0
    print(f"{month:5} | ${payment:.2f}  | ${interest:.2f}    | ${principal:.2f}    | ${remaining:.2f}")



print("Task 2")
for x in range(7):
    for y in range(13):
        if y == 6 - x or y == 6 + x or x == 6:
            print("*",end="")
        else:
            print("",end=" ")
    print()



print("Task 3")
for x in range(5):
    for y in range(5):
        if x == 0 or x == 4 or x + y == 4:
            print("*",end="")
        else:
            print("",end=" ")
    print()