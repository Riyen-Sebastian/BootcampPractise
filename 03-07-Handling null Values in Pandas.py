import pandas as pd
import numpy as np

# Create a sample DataFrame with null values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, np.nan],
    'D': ['a', 'b', np.nan, 'd', 'e']
})

print("Original DataFrame:")
print(df)
print("\n1. Checking for null values:")
print(df.isnull().sum())

print("\n2. Dropping rows with any null values:")
print(df.dropna())

print("\n3. Dropping columns with any null values:")
print(df.dropna(axis=1))

print("\n4. Filling null values with a specific value:")
print(df.fillna(0))

print("\n5. Filling null values with method 'ffill' (forward fill):")
print(df.fillna(method='ffill'))

print("\n6. Filling null values with method 'bfill' (backward fill):")
print(df.fillna(method='bfill'))

print("\n7. Filling null values with column mean:")
print(df.fillna(df.mean()))

print("\n8. Interpolating null values:")
print(df.interpolate())

print("\n9. Replacing null values in specific columns:")
df['D'].fillna('Unknown', inplace=True)
print(df)

print("\n10. Identifying rows with null values:")
print(df[df.isnull().any(axis=1)])