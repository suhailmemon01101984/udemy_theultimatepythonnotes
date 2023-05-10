#any(): returns True if any element in an iterable is true. 
#If the iterable is empty, returns False.

numbers = [0, 1, 2, 3, 4]
has_positive_number = any(num > 0 for num in numbers)
print(has_positive_number) # Output: True

numbers = [0, 0, 0]
has_positive_number = any(num > 0 for num in numbers)
print(has_positive_number) # Output: False
