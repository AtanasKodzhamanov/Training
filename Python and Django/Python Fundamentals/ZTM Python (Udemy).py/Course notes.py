# Random functions
bin(5)  # returns binary

# Encapsulation is keeping data and methods that act on that data together in a single unit (class).
# Abstraction is hiding the complexity of the code from the user. For example, you don't need to know how a car works to drive it. You just need to car.drive() and it will drive. You don't need to know how the drive method works.
# Inheritance is the ability to create a class that inherits all the properties and methods from another class. For example, a car is a vehicle. A car can inherit from the vehicle class and have all the properties and methods of the vehicle class.
# Polymorhpism is the ability to define a generic type of behavior that will (potentially) behave differently when applied to different types of objects. For example, attack() can have different effects depending on the character class. A warrior's attack() will be different than a mage's attack(). Same function name but different effects.

# Use the super() function to inherit from the parent class. super().__init__() will inherit all the properties and methods from the parent class. You can also use super().method() to call a method from the parent class.


def User():
    def __init__(self, name, email):
        self.name = name
        self.email = email


def Wizard(User):
    def __init__(self, name, power, email):
        # inherits any initialisations from User class so you dont have to repeat them
        super().__init__(name, email)
        self.power = power

# introspection is the ability to inspect an object to see what methods and properties it has
