class dog:

    #IN python we override __int__() to create out constructor
    # Its has a double underscore, known as a "dunder" method
    # We take in "self" pass our new object to our __init__
    def __init__(self, breed, age, color, name="default name"):
        self.breed = breed
        self.age = age
        self.color = color
        self.name = name
    
    def bark(self):
        return f"{self.name} is barking"
    
    def __str__(self):
        return f"My name is {self.name}, I am a {self.breed}"
    
ellie = dog("Maltese", 16, "White", "Ellie")

print(ellie)

# Inheritance - I fI have a class tha is based on another class ("is a" relationship)
# can save myself some time by using inheritance

#I pass in the parent class in parenthesis
class Doodle(dog):

    #We still have to use __init__ as our constuctors, but we have to pass things to the parent class in it using super

    def __init__(self, breed, age, color, name="default name", is_dog=True):
        super().__init__(breed, age, color, name) # We call the parent class __init__ using super
        self.is_dog = is_dog

callie = Doodle("Labradoodle", 16, "yellow", "Callie")

print(callie.bark())

