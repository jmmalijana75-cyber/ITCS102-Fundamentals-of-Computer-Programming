#multiple if and elif condition


name = input("Please input your name ---->> ")

age = int(input("Please input your age ---->> "))


if age >= 0 and age <=5 :
        print("That age is considered as INFANT ")

elif age >= 6 and age <=12 :
         print("That age is considered as KID ")

elif age >= 13 and age <=15 :
         print("That age is considered as PRE TEEN ")

elif age >= 16 and age <=19 :
         print("That age is considered as TEENAGER ")

elif age >= 20 and age <=29 :
         print("That age is considered as EARLY ADULTHOOD ")

elif age >= 30 and age <=58 :
         print("That age is considered as ADULT ")

elif age >= 59 and age <=150 :
         print("That age is considered as SENIOR ")

else:
         print("Age is considered as Invalid") 