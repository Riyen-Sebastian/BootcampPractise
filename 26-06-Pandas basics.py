import pandas as pd
import numpy as np

# Creating Pandas Series from different sources

# From a list
fruits = ['apple', 'banana', 'cherry', 'date']
fruit_series = pd.Series(fruits, index=['a', 'b', 'c', 'd'])
print("Series from list:")
print(fruit_series)
print()

# From a NumPy array
temperatures = np.array([20.5, 22.1, 23.4, 19.8])
temp_series = pd.Series(temperatures, index=['Mon', 'Tue', 'Wed', 'Thu'])
print("Series from NumPy array:")
print(temp_series)
print()

# From a dictionary
book_ratings = {'Harry Potter': 4.5, 'Lord of the Rings': 4.7, 'Pride and Prejudice': 4.3}
rating_series = pd.Series(book_ratings)
print("Series from dictionary:")
print(rating_series)
print()

# Exploring Series attributes
print("Attributes of fruit_series:")
print("Index:", fruit_series.index)
print("Values:", fruit_series.values)
print("Data type:", fruit_series.dtype)
print("Size:", fruit_series.size)
print()

# Using common Series methods
print("Common methods on temp_series:")
print("First two elements:", temp_series.head(2))
print("Last two elements:", temp_series.tail(2))
print("Sorted temperatures:", temp_series.sort_values())
print("Average temperature:", temp_series.mean())
print()

# Applying a function to a Series
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_fahrenheit = temp_series.apply(celsius_to_fahrenheit)
print("Temperatures in Fahrenheit:")
print(temp_fahrenheit)