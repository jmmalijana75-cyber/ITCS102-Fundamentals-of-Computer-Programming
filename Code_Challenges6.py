size = int(input("Enter the size of the pattern: "))

for y in range(size):
    for x in range(size):
        if y + x == size -1 or y == x:
            print("*", end="")
        else:
            print(" ", end="")
    print()
