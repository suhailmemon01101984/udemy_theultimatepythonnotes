'''
len(): Using pure python with Python built-in functions

Example usage:

'''

def my_len(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count

my_list = [1, 2, 54, 4, 22]
print(my_len(my_list))  # Output: 5
