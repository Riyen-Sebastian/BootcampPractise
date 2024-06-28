import matplotlib.pyplot as plt

# Data for pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Data for line chart
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 20, 18]

# Create pie chart
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart Example')

# Create line chart
plt.subplot(1, 2, 2)
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Line Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plots
plt.tight_layout()
plt.show()
