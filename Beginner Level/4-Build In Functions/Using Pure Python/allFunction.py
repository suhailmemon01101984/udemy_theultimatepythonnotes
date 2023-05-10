'''
sorted(): Using pure python
'''


def my_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True

my_list = [True, True, False, True]
print(my_all(my_list))  # Output: False


