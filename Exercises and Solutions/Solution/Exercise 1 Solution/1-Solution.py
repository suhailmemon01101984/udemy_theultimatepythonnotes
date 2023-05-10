#Exercise: Celsius to Fahrenheit Conversion



#One way to sole it 

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))   # Output: 32.0
print(celsius_to_fahrenheit(100)) # Output: 212.0


'''
In this exercise, we defined a function celsius_to_fahrenheit that takes a 
single argument celsius. Inside the function, 
we used the conversion formula to compute the corresponding temperature in 
Fahrenheit, and then returned the result.

We tested the function by calling it with two different input values 
(0 and 100) and printing the output.
'''