#Example 1: Timer decorator


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()  # Output: Execution time: 2.0002 seconds



'''
The timer decorator takes a function as input, 
creates a new function that times the execution of the original function, and returns the new function. 
The wrapper function takes arbitrary arguments (*args and **kwargs) 
and passes them to the original function. 
The execution time is calculated using the time module, and the result is printed to the console.

'''