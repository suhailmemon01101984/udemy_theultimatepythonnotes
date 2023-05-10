# Example 4: Print the multiplication table for numbers 1 to 5


for i in range(1, 6):
    print("Multiplication table of", i)
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print()

