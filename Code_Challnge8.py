
rows = int(input("Enter the number of rows: "))

for x in range(rows - 1):
    for y in range(x, rows):
        print(" ", end=" ")
    
    for y in range(x):
        print("*", end=" ")
        
    for y in range(x + 1):
        print("*", end=" ")        
    print()    
    
for x in range(rows):
    for y in range(x + 1):
        print(" ", end=" ")
    
    for y in range(x, rows - 1):
        print("*", end=" ")
        
    for y in range(x, rows):
        print("*", end=" ")        
    print()    
