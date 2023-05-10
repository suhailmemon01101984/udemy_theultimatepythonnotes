'''
Pandas


Pandas is a library for data manipulation and analysis in Python. 
It provides powerful tools for handling tabular data, including support 
for reading and writing data in a variety of formats, 
filtering and sorting data, and performing aggregations and statistical analyses.
Example use case: Load a CSV file and compute summary statistics.
'''

import pandas as pd

data = pd.read_csv('data.csv')
summary = data.describe()

print(summary)

#We need a data.csv file to make this work