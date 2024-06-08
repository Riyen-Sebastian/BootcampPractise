# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Handling multiple exceptions 
try:
    x = int("hello")
except (ValueError, TypeError):
    print("Error: Invalid input")

# Raising exceptions
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e)

# Custom exceptions
class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Value cannot be negative")

try:
    check_value(-5)
except CustomError as e:
    print("Custom error:", e)

# Using finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Operation complete")