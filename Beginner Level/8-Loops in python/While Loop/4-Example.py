# Example 4: Find the first even number in a list


numbers = [1, 3, 5, 7, 8, 9, 10, 12]
i = 0
while numbers[i] % 2 != 0:
    i += 1
print("The first even number is:", numbers[i])
