"""
sorted(): Using pure python
"""


def my_sorted(iterable):
    lst = list(iterable)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

my_list = [1, 5, 3, 2, 4]
print(my_sorted(my_list))  # Output: [1, 2, 3, 4, 5]

