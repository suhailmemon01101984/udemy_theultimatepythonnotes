#Generators

'''
Generators are a special kind of iterator, 
which can be used to generate a sequence of values on-the-fly, 
without storing them in memory. They are defined using a function and the yield keyword.
'''
#Example
# creating a generator function
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# looping through the generator
for i in fibonacci(10):
    print(i)


'''
In this example, we define a generator function fibonacci that generates 
the Fibonacci sequence up to a given number n. 
We use the yield keyword to generate each value in the sequence on-the-fly. 
We can then loop through the generator using a for loop.
'''