# Exercise: Kilogram to Pound Converter

'''
Write a function kg_to_lb that takes in a weight in kilograms and converts it to pounds. 
The conversion factor from kilograms to pounds is 2.20462 lbs per kilogram. 
The function should return the weight in pounds rounded to two decimal places.
'''

def kg_to_lb(kg):
    lb=round((kg*2.20462),2)
    return(lb)

print(kg_to_lb(100))