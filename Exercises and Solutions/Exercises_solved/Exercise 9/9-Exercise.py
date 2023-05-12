# Exercise:  Finding the Maximum Element in an Array

'''
Write a function find_max(numbers) that takes an array of 
integers numbers as input and returns the maximum element in the array.


Example

>>> find_max([5, 3, 8, 1, 9])
9
>>> find_max([4, 7, 2, 6, 1])
7
>>> find_max([-2, 0, 3, -1, 5])
5

Tis question asks us to find the maximum element in an array of integers. 
We can do this by iterating over the array and keeping track of the maximum 
element we have seen so far. At the end of the loop, we return the maximum element.
'''

def find_max(arr):
    max_element=arr[0]
    for num in arr:
       if max_element<num:
           max_element = num
    return(max_element)

print(find_max([5, 3, 8, 1, 9]))
print(find_max([4, 7, 2, 6, 1]))
print(find_max([-2, 0, 3, -1, 5]))

