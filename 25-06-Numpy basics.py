import numpy as np

# Array creation
print("Array creation:")
a = np.array([1, 2, 3, 4, 5])
print("1D array:", a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", b)

c = np.zeros((2, 3))
print("Array of zeros:\n", c)

d = np.ones((2, 2))
print("Array of ones:\n", d)

e = np.arange(0, 10, 2)
print("Array with arange:", e)

# Array attributes
print("\nArray attributes:")
print("Shape of b:", b.shape)
print("Size of b:", b.size)
print("Data type of b:", b.dtype)

# Indexing and slicing
print("\nIndexing and slicing:")
print("First element of a:", a[0])
print("Last element of a:", a[-1])
print("First row of b:", b[0])
print("Second column of b:", b[:, 1])

# Array operations
print("\nArray operations:")
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print("f + g:", f + g)
print("f * g:", f * g)
print("f * 2:", f * 2)

# Broadcasting
print("\nBroadcasting:")
h = np.array([[1, 2, 3], [4, 5, 6]])
i = np.array([10, 20, 30])
print("h + i:\n", h + i)

# Reshaping
print("\nReshaping:")
j = np.arange(12)
k = j.reshape((3, 4))
print("Reshaped array:\n", k)

# Stacking
print("\nStacking:")
l = np.array([1, 2, 3])
m = np.array([4, 5, 6])
print("Vertical stack:\n", np.vstack((l, m)))
print("Horizontal stack:", np.hstack((l, m)))

# Splitting
print("\nSplitting:")
n = np.array([1, 2, 3, 4, 5, 6])
o, p = np.split(n, 2)
print("Split arrays:", o, "and", p)

# Adding and removing elements
print("\nAdding and removing elements:")
q = np.array([1, 2, 3, 4, 5])
r = np.append(q, 6)
print("Append:", r)
s = np.insert(q, 2, 10)
print("Insert:", s)
t = np.delete(q, 2)
print("Delete:", t)