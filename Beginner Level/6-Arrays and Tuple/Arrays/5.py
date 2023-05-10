#Creating an array of boolean values and using logical operations

# Create an array of boolean values
bools = [True, False, True, True, False]

# Using logical operations with arrays
all_true = all(bools)  # Checking if all elements in the array are True
any_false = any([not b for b in bools])  # Checking if any element in the array is False

# Modifying elements in an array using logical operations
bools = [not b for b in bools]  # Inverting all elements in the array

# Looping through an array using logical operations
for b in bools:
    print("Yes" if b else "No")

# Slicing an array of boolean values
first_three_bools = bools[:3]  # Getting the first three elements of the array
last_two_bools = bools[-2:]  # Getting the last two elements of the array

# Printing the arrays
print(bools)
print(first_three_bools)
print(last_two_bools)
