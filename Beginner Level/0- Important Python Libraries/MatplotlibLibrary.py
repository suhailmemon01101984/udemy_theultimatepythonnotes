'''
Matplotlib


Matplotlib is a library for creating static, animated, 
and interactive visualizations in Python. It provides 
a variety of tools for creating line plots, scatter plots, 
bar charts, histograms, and more.

Example use case: Plot a sine wave.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
