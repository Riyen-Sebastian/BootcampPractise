# Lists in python


#list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

words = ["hi", "hello", "hey"]
caps = [word.upper() for word in words]
print(caps)  # ['HI', 'HELLO', 'HEY']

nested = [[1, 2], [3, 4]]
flat = [x for sublist in nested for x in sublist]
print(flat)  # [1, 2, 3, 4]

#Indexing and Slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[2])  # 3
print(numbers[:3])  # [1, 2, 3]
print(numbers[-2:])  # [4, 5]
numbers[1] = 10
print(numbers)  # [1, 10, 3, 4, 5]



#Searching and sorting
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print(fruits.index("cherry"))  # 2

fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry']

fruits.sort(reverse=True)
print(fruits)  # ['cherry', 'banana', 'apple']

#Special Methods
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)  # 15

cubes = list(map(lambda x: x**3, nums[:3]))
print(cubes)  # [1, 8, 27]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

names = ["Alice", "Bob"]
scores = [90, 85]
pairs = list(zip(names, scores))
print(pairs)  # [('Alice', 90), ('Bob', 85)]