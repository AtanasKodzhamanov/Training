# The ability to define a generic type of behavior that will (potentially) behave differently when applied to different types of objects

# __repr__ will return a string representation of the object that can be used to recreate the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self._age})'

    def __str__(self):
        return self.name
# You can call __repr__ by using repr(), str(), print(), or just typing the object name. If you don't define __repr__, it will use the default __repr__ which is the memory address of the object.
# __str__ is similar to __repr__ but it is meant to be more human readable.

# There are also dunder methods for arithmetic operators such as __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __and__, __xor__, __or__
# Also rich comparison operators such as __lt__, __le__, __eq__, __ne__, __gt__, __ge__
# These methods are used between objects. For example, if you have two objects of the same class, you can use __add__ to add them together. You have to def __add__ in the class and use (self, other) where other is the other object you are adding to the first object.
