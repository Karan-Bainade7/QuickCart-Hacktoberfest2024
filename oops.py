# OOP in Python - Demonstrating Major Concepts

# 1. Class and Object
class Animal:
    # Class attributes (shared by all instances)
    kingdom = "Animalia"

    # Constructor (__init__ method) to initialize instance attributes
    def __init__(self, name, species):
        # Instance attributes (unique to each object)
        self.name = name
        self.species = species
    
    # Method (function inside a class) to print info
    def info(self):
        return f"{self.name} is a {self.species}."

# 2. Encapsulation: Keeping data safe within objects
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class (Animal) constructor using super()
        super().__init__(name, "Dog")
        # Private attribute (not accessible directly from outside the class)
        self.__breed = breed
    
    # Getter method (access private attribute)
    def get_breed(self):
        return self.__breed
    
    # Setter method (modify private attribute)
    def set_breed(self, breed):
        self.__breed = breed

# 3. Inheritance: Reusing code from a parent class
class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, "Bird")
        # Adding a unique attribute for the Bird class
        self.can_fly = can_fly

    # Polymorphism: Method overriding (changing behavior of inherited method)
    def info(self):
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"{self.name} is a {self.species} and {fly_status}."

# 4. Polymorphism: Multiple classes with the same method
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, "Fish")

    # Polymorphism: Method overriding
    def info(self):
        return f"{self.name} is a {self.species} and lives in water."

# 5. Abstraction: Using abstract classes and methods (from abc module)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    # Abstract method (forces subclasses to implement it)
    @abstractmethod
    def move(self):
        pass

# Inheriting from abstract class Vehicle
class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

class Boat(Vehicle):
    def move(self):
        print("The boat sails on the water.")

# 6. Demonstrating all concepts together
def main():
    # Creating instances (objects) of different classes
    dog = Dog("Buddy", "Golden Retriever")
    bird = Bird("Tweety")
    fish = Fish("Nemo")

    # Accessing attributes and methods
    print(dog.info())  # From Animal class
    print(f"Breed: {dog.get_breed()}")  # Accessing private attribute using getter
    dog.set_breed("Labrador")  # Modifying private attribute using setter
    print(f"New Breed: {dog.get_breed()}")

    # Demonstrating polymorphism and inheritance
    print(bird.info())  # Overridden method in Bird class
    print(fish.info())  # Overridden method in Fish class

    # Demonstrating abstraction
    car = Car()
    boat = Boat()
    car.move()  # Car class implements abstract method move()
    boat.move()  # Boat class implements abstract method move()

if __name__ == "__main__":
    main()
