# Exercise: Finding the Maximum Element in an Array

'''
Tis question asks us to find the maximum element in an array of integers. 
We can do this by iterating over the array and keeping track of the maximum 
element we have seen so far. At the end of the loop, we return the maximum element.
'''

#Solution


def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Test the function
print(find_max([5, 3, 8, 1, 9]))
print(find_max([4, 7, 2, 6, 1]))
print(find_max([-2, 0, 3, -1, 5]))


'''
In this solution, we initialize max_number to the first element in the array. 
Then, we iterate over the remaining elements in the array and check if each element 
is greater than max_number. 
If it is, we update max_number to the new maximum. Finally, we return max_number.

'''