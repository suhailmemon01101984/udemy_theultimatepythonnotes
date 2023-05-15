#Example 2: Memoization decorator

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55


'''
The memoize decorator takes a function as input, creates a cache dictionary to store the results of the function, 
and returns a new function that checks if the result of the function has already been computed for a given input, 
and returns the cached result if it has, or computes the result and stores it in the cache if it hasn't.

The fibonacci function is a recursive function that calculates the nth number in the Fibonacci sequence. 
The memoize decorator is used to cache the results of the function, 
so that the function doesn't need to be called multiple times for the same input.

'''