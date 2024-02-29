"""
Python class properties
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height


new_rectangle = Rectangle(12, 10)
print(new_rectangle.base)
print(new_rectangle.height)

new_rectangle.base = 5
print()
print(new_rectangle.base)
