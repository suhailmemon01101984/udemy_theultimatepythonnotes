'''
min(): Using pure python with Python built-in functions

Example usage:

'''

def my_min(iterable):
    smallest = iterable[0]
    for item in iterable:
        if item < smallest:
            smallest = item
    return smallest

my_list = [1, 2, 5, 3, 4]
print(my_min(my_list))  # Output: 1



