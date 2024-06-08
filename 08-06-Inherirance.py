# Base class 1
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print(f"Starting {self.fuel_type} engine.")

# Base class 2
class ElectricMixin:
    def charge(self):
        print("Charging electric components.")

# Multiple Inheritance
class HybridCar(Engine, ElectricMixin):
    def __init__(self, model):
        super().__init__("hybrid")  # Calling Engine's __init__
        self.model = model

    def display_info(self):
        print(f"This is a {self.model} hybrid car.")

# Base class for all vehicles
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("Beep beep!")

# Single Inheritance
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Multiple Inheritance with Method Overriding
class HybridSportsCar(HybridCar, Car):
    def __init__(self, brand, model):
        HybridCar.__init__(self, model)
        Car.__init__(self, brand, model)

    def display_info(self):  # Overrides both HybridCar's and Car's method
        print(f"This is a {self.brand} {self.model} hybrid sports car.")

    def turbo_boost(self):
        print("Engaging turbo boost!")



# super() with __init__



# Base class
class Emp:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

# Class Freelancer inherits Emp
class Freelancer(Emp):
    def __init__(self, id, name, address, email):
        super().__init__(id, name, address)  # Using super() to call parent's __init__
        self.email = email

# Creating an instance
emp1 = Freelancer(103, "Suraj Kumar Gupta", "Noida", "SKG@gmail.com")
print('ID:', emp1.id)
print('Name:', emp1.name)
print('Address:', emp1.address)
print('Email:', emp1.email)


# super() with __str__


# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f"I am a {self.species}"

# Child class inherits Parent class (Animal)
class Dog(Animal):
    def __init__(self, breed):
        super().__init__("dog")  # Using super() to call parent's __init__
        self.breed = breed

    def __str__(self):
        return super().__str__() + f" of breed {self.breed}"  # Using super() with __str__

# Creating an instance of Dog
my_dog = Dog("Labrador")

# Printing the Dog instance
print(my_dog)  # Output: I am a dog of breed Labrador