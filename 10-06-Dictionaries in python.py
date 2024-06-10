# Dictionaries in Python


# 1. Creating Dictionaries
empty_dict = dict()
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Person Dictionary:", person)

# 2. Accessing and Modifying Values
print("Name:", person['name'])
print("Age:", person.get('age'))

person['age'] = 31
print("Updated Age:", person['age'])

# 3. Adding and Removing Key-Value Pairs
person['email'] = 'alice@example.com'
print("Added Email:", person)

removed_value = person.pop('city')
print("Removed City:", removed_value)
print("Updated Person:", person)

# 4. Dictionary Methods
keys = person.keys()
values = person.values()
items = person.items()
age = person.get("age","Error")
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
print("Age:", age)

# 5. Dictionary Comprehension
squares = {num: num**2 for num in range(1, 6)}
print("Squares:", squares)

# 6. Nesting Dictionaries
employee = {
    'name': 'John',
    'age': 35,
    'contact': {
        'email': 'john@example.com',
        'phone': '123-456-7890'
    }
}
print("Employee Email:", employee['contact']['email'])