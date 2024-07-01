import matplotlib.pyplot as plt
import numpy as np

# Let's start with a basic line plot
print("Practicing basic line plot...")
x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x**2

plt.plot(x, y)
plt.show()

#for multiple lines in one plot
print("\nNow trying multiple lines in one plot...")
x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6, 3, 2, 3]
plt.plot(x, y, linestyle='-.', marker='*')

x1 = [2, 4, 6, 8, 10]
y1 = [1, 2, 3, 4, 5]
plt.plot(x1, y1, color="red", marker="o")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Multiple plot")
plt.show()

# Subplots 
print("\nPracticing subplots...")
plt.subplot(2, 2, 1)
plt.plot(x, y, 'y')

plt.subplot(2, 2, 2)
plt.plot(x1, y1, color="red", marker="o")

plt.subplot(2, 2, 3)
plt.plot(x, y, 'g')

plt.show()

# Now let's try a more realistic example with ages and salaries
print("\nCreating a plot with ages and salaries...")
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y)
plt.title('Median salaries (INR) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.show()

# Adding more data and a legend
print("\nAdding more data and a legend...")
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(dev_x, dev_y, label='All Developers')
plt.plot(dev_x, py_dev_y, label='Python Developers')

plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.show()

# Formatting the chart
print("\nFormatting the chart...")
plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='x', label='All Developers')
plt.plot(dev_x, py_dev_y, color='r', marker='o', label='Python Developers')

plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.grid(True)
plt.show()

# Final example with three datasets and more formatting
print("\nFinal example with three datasets and more formatting...")
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x, dev_y, color='k', linewidth=3, marker='x', label='All Developers')
plt.plot(dev_x, py_dev_y, color='r', linewidth=3, marker='o', label='Python Developers')
plt.plot(dev_x, js_dev_y, color='b', linewidth=3, marker='X', label='JavaScript Developers')

plt.title('Median salaries (AED) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries')
plt.legend()
plt.grid(True)
plt.show()

print("Finished practicing! That was really informative.")