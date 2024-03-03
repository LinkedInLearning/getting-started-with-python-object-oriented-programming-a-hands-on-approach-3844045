"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        print(f"Circumference: {2 * 3.14 * self.radius} units.")

    def display_area(self):
        print(f"Area: {3.14 * self.radius ** 2} square units.")


# Create an instance of Circle
my_circle = Circle(2)

# Display its circumference and area
my_circle.display_circumference()
my_circle.display_area()
