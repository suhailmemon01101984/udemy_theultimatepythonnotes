# Example 3: Using tuples as dictionary keys
# Create a dictionary with a tuple as a key
person = {("John", "Smith"): 28, ("Jane", "Doe"): 30}

# Access the value for a specific key
john_age = person[("John", "Smith")]

# Add a new key-value pair to the dictionary
person[("Bob", "Johnson")] = 35

# Print the updated dictionary
print(person)
