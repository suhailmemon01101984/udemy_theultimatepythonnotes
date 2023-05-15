#Iterators

'''
An iterator is an object that can be iterated (looped) upon.
 An object which will return data, one element at a time. 
 In Python, an iterator is an object which implements the iterator protocol. 
The iterator protocol consists of two methods: __iter__() and __next__().
'''
#Example
# creating an iterator for a list
lst = [1, 2, 3, 4, 5]
iter_lst = iter(lst)

# looping through the iterator
for i in iter_lst:
    print(i)

'''
In this example, we first create a list lst.
We then create an iterator iter_lst for the list using the iter() function. 
We can then loop through the iterator using a for loop.
'''