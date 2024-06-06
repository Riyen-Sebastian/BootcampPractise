# Python Input and Output Statements

# Input statement
favorite_color = input("Enter your favorite color: ")
print("Your favorite color is", favorite_color)

# Output statement with keyword arguments
print("Welcome", "to", "Python", sep=" * ", end="!!!\n")

# Data Types in Python
int_num = 100
float_num = 9.81
complex_num = 5 + 6j
string = "Learning Python!"
boolean = None
list_example = [True, False, True]
tuple_example = ("Python", "Java", "C++")
dict_example = {"brand": "Toyota", "model": "Corolla", "year": 2020}
set_example = {8, 7, 6}

print(int_num, float_num, complex_num)
print(string, boolean)
print(list_example, tuple_example)
print(dict_example, set_example)

# Expressions and Operators

m = 7
n = 3

# Arithmetic Operators
print(m + n)  # Addition: 10
print(m - n)  # Subtraction: 4
print(m * n)  # Multiplication: 21
print(m / n)  # Division: 2.333...
print(m // n) # Floor Division: 2
print(m % n)  # Modulus: 1
print(m ** n) # Exponentiation: 343

# Comparison Operators
print(m == n) # Equal to: False
print(m != n) # Not equal to: True
print(m > n)  # Greater than: True
print(m < n)  # Less than: False
print(m >= n) # Greater than or equal to: True
print(m <= n) # Less than or equal to: False

# Logical Operators
print(m > 5 and n < 5)  # and: True
print(m > 10 or n < 5)  # or: True
print(not(m > 5 and n < 5)) # not: False

# Type Casting
int_from_str = int("123")
float_from_str = float("45.67")
str_from_float = str(8.90)
list_from_tuple = list((4, 5, 6))
tuple_from_dict = tuple({"key1": "value1", "key2": "value2"}.keys())

print(int_from_str)
print(float_from_str)
print(str_from_float)
print(list_from_tuple)
print(tuple_from_dict)

# Conditional Statements
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Looping Statements
# For loop
languages = ["Python", "JavaScript", "Ruby"]
for language in languages:
    print(language)

# While loop
number = 5
while number > 0:
    print("Countdown:", number)
    number -= 1

# Jumping Statements
# break statement
for i in range(1, 11):
    if i == 8:
        break
    print(i)

# continue statement
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# Special Functions
# len() function
length_of_tuple = len((10, 20, 30))
print("Length of tuple:", length_of_tuple)

# id() function
unique_id = id(42)
print("Unique ID of 42:", unique_id)

# type() function
type_of_variable = type([1, 2, 3])
print("Type of [1, 2, 3]:", type_of_variable)

# range() function
range_example = range(0, 20, 5)
print("Range example:", list(range_example))
