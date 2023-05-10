#Creating an array of mixed types


# Create an array of mixed types
mixed = [1, "two", 3.0, True, [4, 5, 6]]

# Accessing elements in an array
first_item = mixed[0]  # Accessing the first element in the array
last_item = mixed[-1]  # Accessing the last element in the array

# Modifying elements in an array
mixed[1] = 2  # Changing the second element in the array to 2
mixed.append("seven")  # Adding a new element to the end of the array

# Looping through an array
for item in mixed:
    print(item)

# Slicing an array
first_three_items = mixed[:3]  # Getting the first three elements of the array
last_two_items = mixed[-2:]  # Getting the last two elements of the array

# Printing the arrays
print(mixed)
print(first_three_items)
print(last_two_items)
