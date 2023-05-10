'''
sum(): returns the sum Using pure python with Python built-in functions
'''
def my_sum(iterable):
    total = 0
    for item in iterable:
        total += item
    return total

my_list = [1, 2, 3, 4, 5]
print(my_sum(my_list))  # Output: 15
