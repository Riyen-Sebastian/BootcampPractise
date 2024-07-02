import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the style for our plots
sns.set_style("whitegrid")

# Create a sample dataset
np.random.seed(0)
data = pd.DataFrame({
    'x': np.random.normal(0, 1, 100),
    'y': np.random.normal(0, 1, 100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='x', y='y', hue='category')
plt.title('Scatter Plot with Categories')
plt.show()

# Create a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='category', y='y')
plt.title('Box Plot of Y by Category')
plt.show()

# Create a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='x', kde=True)
plt.title('Histogram of X with KDE')
plt.show()

# Create a pair plot
sns.pairplot(data, hue='category')
plt.suptitle('Pair Plot of All Variables', y=1.02)
plt.show()

# Create a heatmap
correlation = data[['x', 'y']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()