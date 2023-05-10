'''
max(): Using pure python with Python built-in functions

Example usage:

'''

def my_max(iterable):
    largest = iterable[0]
    for item in iterable:
        if item > largest:
            largest = item
    return largest

my_list = [1, 2, 5, 3, 4, 9]
print(my_max(my_list))  # Output: 9



