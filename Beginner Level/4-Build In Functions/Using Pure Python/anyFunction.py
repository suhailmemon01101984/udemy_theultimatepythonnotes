'''
any(): Using pure python
'''


def my_any(iterable):
    for item in iterable:
        if item:
            return True
    return False

my_list = [False, False, True, False]
print(my_any(my_list))  # Output: True


