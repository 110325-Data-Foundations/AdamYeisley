# This is a comment, even if there is valid code in here the interpreter will ignore it.
# Add comments frequently and descriptively

# Data types: booleans, strings, float, Char, integer, null

# Python data types: 
# String - string of characters
# num, 
    #int - whole numbers
    #float - floating point numbers
# boolean - true/false values
# none

# If I want to declare a variable:

myNum = 11

# No ; needed

nyNum2:int = 12

# The :int is a type hint for myself and others

# Name variables appropriately, no x, y, z, etc. Make them meaningful.

#numerical types: int and float

my_int = 1 #No decimals
my_float = 1.1 #Decimals

#Strings are for words and text
my_String = "Some words!"

#Boolean true/flale

true_boolean = True
false_boolean = False

#None is a intentionally empty variable

my_none = None

#We can use arithmatic operators with numerical types

sum = my_int + my_float
print(sum)

# + operator can do string concatination, better method follows with formatting

name = "Adam"
greeting = "Hello " + name

print(greeting)

# It is clearer to use formatted strings for this task

formatted_greeting = f"Hello {name}"

print(formatted_greeting)

# Opperators +, -, /, *
# ** (to the power of)
# % (same as /, but gives remainder)
# // (floor division, rounds down)
# == comparison/equality

# There are no Python primitive types, they are all objects

# Console input and output

#Output to the console is easy in python there is a built in method called print().

print("Here is my console output")

my_input = input()

#Terminal waits for response and prints input with statement below

print(f"User typed {my_input}")

#Falsy values
#Flase
#non3
#0 , 0.0
#""
# empty collections ( lists tables dictionary)

#Truthy values
#... everything else

#casting
#type conversion

#implicit conversion happens automatically

num = 1
num2 = 1.5
my_num = num + num2

#Explicit conver, tell tje interpretor what to do
#in this case, cast my_num as a string
my_message = "My total is: " + str(my_num)

print(my_message)

#Explicit conversion from string to int
ny_new_num = int("123")

#colections

#Python has built in collection types for storing multiple objects at once
#Lists, Sets, dictionaries, range, etc

#List - mutable (editable), allows duplicates, indexable

my_list = [11, 1, 400, 48]

#append adds new list item

my_list.append("appended text")

#extension adds a collection of objects to my list

my_list_extension = [2345]

my_list.extend(my_list_extension)

#insert

my_list.insert(3, "inserted text")

#Removes first instance of value passed to .remove

my_list.remove(1)

#pop removes the last thing in the list

my_list.pop()

#you can also pop by index

my_list.pop(1)

#reverses the list

my_list.reverse()

#sort won't work since strings can't be <> integers

#my_list.sort()

print(my_list)

#sets - mutable, doesn't allow duplicates, indexable (not working with [0]), searchable

my_set = {1, 2, 3}

my_set.add(5)

#below duplicate is ignored since it is already in set

my_set.add(1)

print(my_set)

#this pop doesn't keep the first num (1) in the set in the second print
# unlike a list, pop is first in first out when dealing with sets
print(my_set.pop())

print(my_set)

# i can use remove and discard to remove specific values from my set
#notice we say remove values, not remove the value at an index

#remove will raise an error if the given value doesn't exist in the set
my_set.remove(2)
my_set.discard(3)

print(my_set)

#ADD MISSING NOTES HERE

# Dictionary
# Collections of key/value errors. JUst about any data type can be used for keys and values.
#They are mutable and you can have duplicate values, but keys must be unique
# Semantics: maybe keys were always indexes? But rece


my_dictionary = {
    "key": "value",
    100:1000,
    None:"This will still work",


}

print(my_dictionary)

#adding a new key value pair to the dictionary
my_dictionary["new key"] = 23

print(my_dictionary)