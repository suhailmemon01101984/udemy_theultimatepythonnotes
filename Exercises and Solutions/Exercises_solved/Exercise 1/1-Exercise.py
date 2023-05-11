# Exercise: Celsius to Fahrenheit Conversion

'''
Write a function celsius_to_fahrenheit that takes a temperature 
in Celsius as an argument and returns the temperature in Fahrenheit. 

The conversion formula is F = C * 9/5 + 32.

For example, celsius_to_fahrenheit(0) should return 32.0, 
and celsius_to_fahrenheit(100) should return 212.0.
'''

#Template

def celsius_to_fahrenheit(c):
    return((c*9/5)+32)

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
