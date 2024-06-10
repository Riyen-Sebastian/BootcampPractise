#Tuples on python

# Tuples: Store multiple items in a single variable
my_tuple = ("pizza", 42, True)
print("My favorite things:", my_tuple)

# Indexing: Access elements by their position
first_item = my_tuple[0]
print("First item:", first_item)

# Slicing: Get a range of elements
numbers = (1, 2, 3, 4, 5)
some_numbers = numbers[1:4]
print("Some numbers:", some_numbers)

# Count: Find how many times an item appears
fruits = ("apple", "banana", "apple", "cherry")
apple_count = fruits.count("apple")
print("Number of apples:", apple_count)

# Index: Find the position of an item
banana_index = fruits.index("banana")
print("Index of banana:", banana_index)



# Tuple immutability: Can't change items
try:
    my_tuple[0] = "burger"
except TypeError as e:
    print("Can't change tuples:", e)

# Joining tuples
more_fruits = ("orange", "kiwi")
all_fruits = fruits + more_fruits
print("All fruits:", all_fruits)

# Multiplying tuples
multiplied_fruits = fruits * 2
print("Multiplied fruits:", multiplied_fruits)

# Using asterisk for unpacking
green, *tropic, red = ("apple", "mango", "papaya", "pineapple", "cherry")
print("Green:", green, "Tropic:", tropic, "Red:", red)

# Looping through tuples
for fruit in fruits:
    print("I like", fruit)

# Tuple vs List
my_list = [1, 2, 3]
my_list[1] = 20
print("Changed list:", my_list)

# When to use tuples: immutable data, data integrity
settings = ("localhost", 8080, "debug")
print("Settings (won't change):", settings)

# Built-in functions
lengths = len(my_tuple)
print("Length of my_tuple:", lengths)

sum_numbers = sum(numbers)
print("Sum of numbers:", sum_numbers)

max_fruit = max(fruits)
print("Max fruit:", max_fruit)

min_fruit = min(fruits)
print("Min fruit:", min_fruit)

sorted_fruits = sorted(fruits)
print("Sorted fruits:", sorted_fruits)

# Count and Index with various data types
mixed_tuple = (0, 1, (2, 3), (2, 3), 1, [3, 2], 'geeks', (0,))
print("Count of (2, 3):", mixed_tuple.count((2, 3)))
print("Index of 'geeks':", mixed_tuple.index('geeks'))

try:
    print(mixed_tuple.index(4))
except ValueError:
    print("4 not found in tuple")

