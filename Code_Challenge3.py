print("PACKAGE DETAILS")
Y = "YES"
N = "NO"


sdn = (input("\nSENDER NAME: ")) #sender name
top = (input("TYPE OF PRODUCT: "))# type of product

frag = (input("FRAGILE? (YES / NO): ")) #fragile
if frag == Y:
  print("Fragile: TRUE")
elif frag == N:
  print("Fragile: FALSE")


print("\nPRODUCT DETAILS")

wkg = eval(input("WEIGHT(kg): ")) #weightinkg
dist = eval(input("DISTANCE(km): ")) #distance

basco = (wkg * 2.50) + (dist * 0.15)
exp = (input("EXPRESS (YES / NO): "))
if exp == Y:
  print("Express: TRUE")
elif exp == N:
  print("Express: FALSE")
int = (input("INTERNATIONAL (YES / NO): "))
if int == Y:
  print("International: TRUE")
elif int == N:
  print("International: FALSE")

if wkg<= 2 and dist<= 100: #SHIPPING FREE
  total1 = 0.00
  print("\nThe Shipping is Free\nThe Cost of Package: $",total1)
elif exp == Y and int == Y : #INTERNATIONAL AND EXPRESS
  total2 = (basco * 1.40) + 50
  print("\nThe Product is Both International & Express\nThe Cost of the Package: $",total2)
elif wkg>= 20 and exp == Y or int == Y : # EXPRESS OR HEAVY INTERNATIONAL
  total3 = (basco * 1.20) + 25
  print("\nThe Product is Express or Heavy International\nThe Cost of the Package: $",total3) 
elif wkg>= 30 or dist>= 1000: #OVERSIZED/FAR
  total4 = basco + 30
  print("\nThe Product is Oversized/Far\nThe Cost of the Package: $",total4)
else: 
  print("\nThe Product Standard Rate: $",basco)