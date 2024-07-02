import matplotlib.pyplot as plt
import numpy as np

print("Let's explore different types of charts with matplotlib,")

# Bar Chart
print("\nCreating a bar chart...")
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 35, 14, 27, 10]

plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Bar Chart with Line Chart
print("\nNow, let's combine a bar chart with a line chart...")
x = np.arange(len(categories))
line_values = [20, 25, 30, 35, 40]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(x, values, align='center', alpha=0.8)
ax1.set_xlabel('Categories')
ax1.set_ylabel('Bar Values')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

ax2 = ax1.twinx()
ax2.plot(x, line_values, color='red', marker='o')
ax2.set_ylabel('Line Values')

plt.title('Bar Chart with Line Chart')
plt.show()

# Scatter Plot
print("\nCreating a scatter plot...")
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(10, 6))
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

# Histogram
print("\nLet's make a histogram...")
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Normal Distribution 
print("\nPlotting a normal distribution...")
def normal_distribution(x, mean, std_dev):
    return np.exp(-((x - mean)**2) / (2 * std_dev**2)) / (std_dev * np.sqrt(2 * np.pi))

x = np.linspace(-5, 5, 100)
y = normal_distribution(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.show()

# Box Plot
print("\nFinally, let's create a box plot...")
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(10, 6))
plt.boxplot(data)
plt.title('Box Plot')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.show()

