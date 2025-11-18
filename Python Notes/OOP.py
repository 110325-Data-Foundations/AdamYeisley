# The Four Pillars of OOP
    # APIE
# Abstraction: The hiding of implementation details
# Example: Don't need to know how the car works, just how to drive it.

# Polymorphism
# It has many forms
# Animals to child class dog
# Overloading: Add or remove some parameters
# Example:

# Overriding: Same parameters to change functionality
# Example:

# Inheritance: Child class inheriting from parent class
# Example:

# Encapsulation: Bundling properties and methods
# Example : Cats meow, sleep, and purr. We can bundle into a cat class.


# VENV
# TO start virtual environment:
# 1. .venv/Scripts/activate
# 2. Make new terminal
# 3. New terminal should say: source C:/Users/ovoad/OneDrive/Desktop/AdamYeisley_main/.venv/Scripts/activate (.venv) 

# Last week we saw inheritance between two concrete clases
# Both of these classes provided for object instantination as well as method implementation

# WHat if I wanted a clas to enforce developer behavior but not allow for implementation?

# In order to use Abstract classes, I need to import ABC ( ABstract base class)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    #Abstract method: a method that needs to be implemented by any child classes, we don't provide for implementation
    #within our abstract class
    @abstractmethod # This decorator lets the interpreter know this method is abstract
    def move():
        pass # This is just a placeholder for a Null operation- essentially telling the interpreter nothing happens here on purpose

# Unlike the abstract method above, this method is concrete, any children will inherit this default implementation
    def break_down():
        print("Something went wrong...")

    # Since we don't have an __init__, we can't create abstract oroperties the way we expect to
    # We have to make use of decorators

    @property
    @abstractmethod # Things are getting weird...
    def vin(self): # This is how I'd create an abstract properti
        pass # It looks like an abstarct method, but with the property decorator layered on top.

class Car(Vehicle):

    def __init__(self, make, model, year, value, vin):
        self.make = make
        self.model = model
        self.year = year
        self.value = value
        self._vin = vin # Notice, no super() call here - vehicle() never orrose __init__()
    
    #providing implementations for move()
    def move():
        print("We start driving")
    
    @property # Using this to be different from a method
    def vin(self, value):
        self._vin = value #Kind of ugly, but this is how python provides for abstract properties
    #Taken in from the intit, set it as normal, then define what appears to be a getter method.


my_car = Car("Toyota", "Prius", 2020, 50000, "13413j41jkkjb1432")

print(my_car.__dict__)

my_car._vin # Underscore technically means intenral or protected: python doesn't care

class Animal:
    def __init__(self, name, age, species, secret, super_secret):
        self.name = name
        self.age = age
        self.species = species # This is just public - the default
        self._secret = secret # This underscore is a convention, it is not enforced by the interpreter, its for us
        self.__super_secret = super_secret # This double underscore is python's version of "private"
        # Enforced by the interpreter as best it can 

        # Under the hood, the __field uses name mangling, it auto alters the name of this property
        # my_animal.__super_secret - not valid
        # my_animal._Animal__super_secret - this is the post name-mangling name of the property