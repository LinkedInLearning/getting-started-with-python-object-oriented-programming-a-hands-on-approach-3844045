"""
Python Polymorphism example
"""


class ClassA:
    def my_lovely_method(self):
        print("my_lovely_method() from ClassA")


class ClassB(ClassA):
    def my_lovely_method(self):
        print("my_lovely_method() from ClassB")

obj_a = ClassA()
obj_b = ClassB()
obj_a.my_lovely_method()
obj_b.my_lovely_method()

