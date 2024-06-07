#implementing oops as calculator program

# 1. OOP in Python
# OOP is a programming style that uses objects to organize code.

# 2. General OOPs vs Python OOPs
# Python's implementation of OOP is straightforward and easy to implement

# 3. Class and Object
class BasicCalculator:#class
    def __init__(self, brand):
        self.brand = brand

calc1 = BasicCalculator("MathMaster")#object
print("Calculator brand:", calc1.brand)

# 4. Data Members in Class
class CalculationTracker:
    total_calculations = 0  # Class variable

    def __init__(self):
        self.user_calculations = 0  # Instance variable

    def track_calculation(self):
        self.user_calculations += 1
        CalculationTracker.total_calculations += 1

tracker1 = CalculationTracker()
tracker1.track_calculation()
print("Total calculations:", CalculationTracker.total_calculations)

# 5. Methods in Class
class ArithmeticUtils:
    @staticmethod
    def add(a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

math_utils = ArithmeticUtils()
print("5 + 3 =", ArithmeticUtils.add(5, 3))
print("4 * 6 =", math_utils.multiply(4, 6))

# 6. Special Methods
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

frac1 = Fraction(3, 4)
print("Fraction:", frac1)

# 7. Constructor and Deconstructor
class TemporaryCalculation:
    def __init__(self, result):#constructor
        print("Calculation result", result, "stored.")
        self.result = result

    def __del__(self):#deconstructor
        print("Calculation result", self.result, "cleared.")

temp_calc = TemporaryCalculation(10)
del temp_calc

# 8. Methods with Arguments
class AdvancedCalculator:
    def power(self, base, exponent):
        print(base, "raised to", exponent, "is", base ** exponent)

adv_calc = AdvancedCalculator()
adv_calc.power(2, 3)

# 9. Data Encapsulation :makes the entire system a single unit which relays over roles, but keeps internal mechanisms hidden 
class SecureCalculator:
    def __init__(self):
        self.__last_result = 0

    def add(self, a, b):
        self.__last_result = a + b
        return self.__last_result

    def get_last_result(self):
        return self.__last_result

secure_calc = SecureCalculator()
print("3 + 5 =", secure_calc.add(3, 5))
print("Last result:", secure_calc.get_last_result())

# 10. Data Abstraction: only the nessecary amont of info is revealed during execution
class Shape:
    def area(self):
        pass  # Abstract method, to be implemented by subclasses

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(5)
print("Area of square with side 5:", square.area())

# 11. Data Hiding
class PasswordProtectedCalculator:
    def __init__(self):
        self.__password = "1234"

    def calculate(self, operation, a, b):
        if self.__check_password():
            if operation == "+":
                return a + b
            elif operation == "*":
                return a * b
        else:
            return "Access denied."

    def __check_password(self):
        return True  # In a real scenario, you'd validate user input

pp_calc = PasswordProtectedCalculator()
print("5 + 3 =", pp_calc.calculate("+", 5, 3))
# print(pp_calc.__password)  # This would raise an AttributeError
print("Bye")