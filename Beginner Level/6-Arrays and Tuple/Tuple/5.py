# Example 5: Creating a tuple of mixed data types
mixed_tuple = (1, "apple", True, 3.14)

# Accessing elements in a tuple
# Get the second element of the mixed_tuple
second_element = mixed_tuple[1]

# Example 3: Looping through a tuple
# Print all the elements of the mixed_tuple
for item in mixed_tuple:
    print(item)

# Unpacking a tuple
# Unpack the first and last elements of the mixed_tuple
first, *middle, last = mixed_tuple
print(first)
print(middle)
print(last)

# Combining tuples
# Create two tuples
numbers = (1, 2, 3)
letters = ("a", "b", "c")

# Concatenate the two tuples into a new tuple
combined_tuple = numbers + letters
print(combined_tuple)
