# Functions - great way to package useful/decrete functionality so you can re-ues it when needed

# Creating a function use the "def" keyword, name the function, give it a paraeter list
# Write the functions code below

#I can even add a return type (at the end ->), interpreter doesnt care though
def addition_function(x:int,y:int) -> int:
    return x + y

def bark(): #TAkes no parameters and doesn't return anything
    print("bark")

sum = addition_function(5,10)

bark()

print(sum)

print(addition_function("first","second")) # If you call strings they concatinate

# Scope: Area of the code where some object/function can be called on and used

# Local

# Enclosed

# Global

# BUilt-In: default python methods and all of the keywords live here, can be accessed
# From anywhere in your code, in any python file. This is where print() lives

#Globale: Accessed anywhere in the file. They are declared in - as well as in other files
# if brought in via import

#This variable is global. I can refrence it inside any blocks

my_dog = "pancake"

# Local: If i have a block of code (some sort of function or flow cotrl block) and i declare a varibale in it-
# That object has local scope

#THis function has its own code block - anything underneath it that is indented

def local_and_closed():
    dog = "tripod"
    my_dog = "banana" # since my dog is gloabl, it can be used in this function

#Print(dog) - can't work with above because it won't be available outside the function, only inside of it

#Enclosed
    def enclosed(): # This function is enclosed within the outer function local_and_closed
        dog = "ollie"
        print(dog)


