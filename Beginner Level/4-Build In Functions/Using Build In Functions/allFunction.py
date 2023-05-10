'''
all(): returns True if all elements in an iterable are true. 
If the iterable is empty, returns True.
'''

numbers = [1, 2, 3, 4]
all_positive_numbers = all(num > 0 for num in numbers)
print(all_positive_numbers) # Output: True

numbers = [1, 2, -3, 4]
all_positive_numbers = all(num > 0 for num in numbers)
print(all_positive_numbers) # Output: False
