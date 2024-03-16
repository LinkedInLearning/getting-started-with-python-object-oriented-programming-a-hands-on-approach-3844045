"""
Challenge: Class Inheritance

Create two subclasses: 'Dog' and 'Cat', which inherit from 'Animal'.

Add additional methods:

wag_tail() for Dog and purr() for Cat
"""

# Base class


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# Subclass Dog

# Subclass Cat


# Create instances
my_dog = Dog("Dusty", "Woof")
my_cat = Cat("Suki", "Meow")

# Call make_sound method and additional methods
my_dog.make_sound()
my_dog.wag_tail()

my_cat.make_sound()
my_cat.purr()
