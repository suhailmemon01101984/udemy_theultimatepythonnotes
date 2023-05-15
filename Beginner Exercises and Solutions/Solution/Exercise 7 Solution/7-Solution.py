# Exercise: Kilogram to Pound Converter

'''
In this solution, we defined a function kg_to_lb that 
takes in a weight in kilograms as an argument, 
converts it to pounds using the conversion factor of 2.20462, 
and returns the weight in pounds rounded to two decimal places using the built-in round() 
function. We then tested the function with some example weights using the print() 
function to output the results to the console.
'''


#One Solution
def kg_to_lb(weight_kg):
    """
    Convert a weight in kilograms to pounds.
    """
    weight_lb = weight_kg * 2.20462
    return round(weight_lb, 2)
    
# Test the function with some example weights
print(kg_to_lb(10))   # Output: 22.05
print(kg_to_lb(100))  # Output: 220.46
print(kg_to_lb(50))   # Output: 110.23

