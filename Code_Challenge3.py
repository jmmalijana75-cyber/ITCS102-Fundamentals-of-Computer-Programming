print("=====PACKAGE DETAILS=====")

Y = "YES"
N = "NO"


sn = (input("\nSender Name:     "))
top = (input("Type Of Product:   "))

frag = (input("Fragile? (YES / NO): "))
if frag == Y:
  print("The product is Fragile")
elif frag == N:
  print("The product is Non-Fragile")
else:
  print("Unidentified")

print("\n\n=====Product Details=====")
wkg = eval(input("Weight(kg):     "))
dkm = eval(input("Distance(km):  "))

base = ("wkg * 2.50") + ("dist * 0.15")
print("The base cost of package: ₱",base)

exp = input("Express (YES / NO): ")
if exp == Y:
  print("Express: True")
elif exp == N:
  print("Express: False")
else:
  print(exp,"UNIDENTIFIED")