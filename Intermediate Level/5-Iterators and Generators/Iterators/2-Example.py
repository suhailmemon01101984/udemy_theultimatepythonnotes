#Example 2: Iterator using built-in iter() and next() functions

numbers = [1, 2, 3, 4, 5]

# Create an iterator using the iter() function
my_iter = iter(numbers)

# Use the next() function to iterate through the iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5
