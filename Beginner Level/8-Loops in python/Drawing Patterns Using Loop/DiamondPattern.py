size = 5
for i in range(size):
    for j in range(size-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
for i in range(size-2, -1, -1):
    for j in range(size-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
