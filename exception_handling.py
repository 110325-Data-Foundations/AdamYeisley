# Errors vs Exceptions

# Error
# Example: my_string = str ing

# Exception - is raised during run time
user_number = int(input())

print(user_number)

# We can handle exception that arise during run time with try-except blocks

# Place the potentially offending code inside the try block
try:
    user_number = int(input()) # This code could raise an exception based on user input
except: # This code only runs if an exception is raised
    print("Please enter a integer")

# I can have as many except blocks as I needm if I want to create multiple exceptions

try:
    user_number = int(input())
except ValueError:
    print("Please enter a integer")
except ZeroDivisionError:
    print("Can't divide by zero")
except: # Always a good idea to end with a generic except block
    print("How did you even trigger this?")

# If we need to we can create custom exceptions based on business rules, not related to python or arithmetic rules.

class MyException(Exception): # A custom excpetion is just a class that inherits from the exception class
    # Like any other class, we need to override __init__ to create this object
    def __init__(self, message="Time to lock in buddy."):
        self.message = message

try:
    print("Please enter an integer")
    user_num = input()

    # If this condition is not true...

    if isinstance(user_num, int): #Check if user entered integer
        raise MyException() # If we get here, manually raise this exception

    print(user_num)
except MyException:
    print("Caught my custom exception")
except:
    print("Caught something else")