#  Functions in Python

# 1) Syntax of a Function
def observe_planet(planet_name):
    """This function prints an observation message."""
    print("Observing the planet", planet_name + "!")

# Function call
observe_planet("Mars")

# 2) Parameters in Functions
def calculate_gravity(mass, radius):
    """This function calculates gravitational force."""
    G = 6.674 * 10**-11  # Gravitational constant
    return (G * mass) / (radius ** 2)

# Positional arguments
gravity = calculate_gravity(5.972 * 10**24, 6371 * 10**3)
print(gravity)

# Keyword arguments
gravity = calculate_gravity(mass=5.972 * 10**24, radius=6371 * 10**3)
print(gravity)

# 3) Return Statement
def distance_to_star(light_years):
    """This function converts light years to kilometers."""
    kilometers_per_light_year = 9.461 * 10**12
    return light_years * kilometers_per_light_year

# Function call
distance = distance_to_star(4.24)
print(distance)

# 4) Default Parameters
def star_brightness(star_name, magnitude=1.0):
    """This function prints the brightness of a star."""
    print("The star", star_name, "has a brightness magnitude of", magnitude)

# Calling with both arguments
star_brightness("Sirius", -1.46)

# Calling with only the required argument
star_brightness("Sirius")

# 5) Variable-Length Arguments
def list_galaxies(*args):
    """This function lists all galaxies passed as arguments."""
    for galaxy in args:
        print("Galaxy:", galaxy)

list_galaxies("Milky Way", "Andromeda", "Triangulum")

def galaxy_info(**kwargs):
    """This function prints galaxy information."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

galaxy_info(name="Andromeda", distance="2.537 million light years", type="Spiral")

# 6) Lambda Functions
# Lambda function to calculate the escape velocity
escape_velocity = lambda mass, radius: (2 * 6.674 * 10**-11 * mass / radius)**0.5

# Calling the lambda function
print(escape_velocity(5.972 * 10**24, 6371 * 10**3))  # Earth's escape velocity

# Lambda function for filtering stars by brightness
stars = [("Sirius", -1.46), ("Canopus", -0.74), ("Arcturus", -0.05)]
bright_stars = list(filter(lambda star: star[1] < 0, stars))
print(bright_stars)

# 7) Function Annotations
def star_temperature(star: str) -> float:
    """This function estimates the temperature of a star in Kelvin."""
    temperatures = {"Sirius": 9940, "Canopus": 7350, "Arcturus": 4286}
    return temperatures.get(star, "Unknown star")

# Calling the function
print(star_temperature("Sirius"))

# 8) Recursion
def count_stars(n):
    """This function recursively counts down the stars."""
    if n == 0:
        print("No more stars to count.")
    else:
        print("Star", n)
        count_stars(n-1)

# Function call
count_stars(5)

# 9) Scope of Variables
def observe():
    """This function demonstrates local scope."""
    constellation = "Orion"
    print("Observing the constellation:", constellation)

constellation = "Cassiopeia"
observe()
print("Outside function:", constellation)  # This will not affect the value inside the function
