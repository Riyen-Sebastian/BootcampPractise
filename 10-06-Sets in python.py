#Sets in python

# Creating sets
my_set = {1, 2, 3, 4, 5}
another_set = set([4, 5, 6, 7, 8])

print("Set created using '{}':", my_set)
print("Set created using set constructor:", another_set)

# Union
grocery_list = {"apples", "bananas", "milk", "bread"}
household_list = {"detergent", "paper towels", "milk", "bread"}
shopping_list = grocery_list | household_list
print("Shopping list:", shopping_list)

# Intersection
hiking_group = {"hiking", "camping", "outdoors"}
photography_group = {"photography", "editing", "hiking"}
common_interests = hiking_group & photography_group
print("Common interests of both groups:", common_interests)

# Difference
recommended_books = {"The Catcher in the Rye", "1984", "To Kill a Mockingbird", "Harry Potter"}
read_books = {"1984", "Harry Potter"}
unread_books = recommended_books - read_books
print("Books that have been read:", unread_books)

# Symmetric Difference
restaurant1_menu = {"pizza", "pasta", "salad", "garlic bread"}
restaurant2_menu = {"pasta", "burger", "fries", "ice cream"}
unique_choices = restaurant1_menu ^ restaurant2_menu
print("Unique Dishes:", unique_choices)

# Adding and Removing Elements
my_set = {1, 2, 3}
print("Before add():", my_set)
my_set.add(4)
print("After add():", my_set)

my_set.remove(2)
print("After remove():", my_set)

# Discarding an element (does not raise an error if the element is not found)
my_set.discard(2)
print("After discard():", my_set)

# Checking if a set is a subset of another
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}
print("Is small_set a subset of big_set?", small_set.issubset(big_set))

# Checking if a set is a superset of another
print("Is big_set a superset of small_set?", big_set.issuperset(small_set))

# Checking if two sets are disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))

# Membership Testing
my_set = {1, 2, 3, 4, 5}
print("Is 3 in my_set?", 3 in my_set)
print("Is 6 in my_set?", 6 in my_set)

# Set Comprehensions
squares = {x * x for x in range(1, 6)}
print("Squares:", squares)

even_squares = {x * x for x in range(1, 6) if x % 2 == 0}
print("Even Squares:", even_squares)

# Unique Interests
user_interests = {
    'Alice': {'sports', 'music', 'reading'},
    'Bob': {'movies', 'music', 'gaming'},
    'Charlie': {'sports', 'music', 'cooking'},
    'David': {'sports', 'traveling', 'photography'},
    'Emma': {'music', 'reading', 'cooking'}
}
unique_interests = {interest for interests in user_interests.values() for interest in interests}
print("Unique Interests:", unique_interests)

# Cartesian Product
set1 = {1, 2}
set2 = {'a', 'b', 'c'}
cartesian_product = {(x, y) for x in set1 for y in set2}
print("Cartesian Product:", cartesian_product)

# Power Set
def power_set(s):
    if len(s) == 0:
        return {frozenset()}
    element = s.pop()
    subsets = power_set(s)
    return subsets.union({subset.union({element}) for subset in subsets})

my_set = {1, 2, 3}
print("Power Set:", power_set(my_set))

# Frozen Set (immutable set)
my_set = {1, 2, 3}
frozen_set = frozenset(my_set)
print("Frozen Set:", frozen_set)


