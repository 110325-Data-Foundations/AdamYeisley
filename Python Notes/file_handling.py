# Python Module - a .py file with some code

#Put imports at the top of your code
# Import the json module
import json

# Import a file
import classes_objects 

# I can get more specific as to what I want to import
from classes_objects import dog





# File handling in Python

# We can interact with files directly from within our app
# This is useful for things like txt files, JSON files, and even things that come in 
# As binary streams such as images

#Default mode is "read" mode

#my_file = open("test-file.txt")

# Open takes two args, one is optional
# The first is the name of the file, if you want it to be created in the same directory as your .py file
# I can also give it a relation

# The second thing we can optinoally pass is a mode
# r - read - opens file for reading (default)
# w - write - opens a file for writing
# a - append - opens the file for appending, if the file exists, it write onto the end of the file
# x - create - creates a file we can work with later, will raise an exception if the file already exists

# By default, Python assumes we are reading a file as text, to work with other types of non-text files, we can use binary code
# rb - read binary
# wb - write binary
# This would be for working with .jpg or .png

# w and a will create a file silently if it doesn't already exist.


my_file = open("./test-file.txt" , "w") 

my_file.write("Hello from my file")

my_file.close() # Usually a good idea to close your file after you work with it

with open("./test-file.txt") as file:
    file_contents = file.read() # Reads the file as a string
    print(file_contents)

# Using the above auto-closes my file

# Working with JSON, they end in .json, but really are just strings

with open("./AdamYeisley/ellie.json", "w") as jsonfile:
    # By default, the built in json module can map certain data type/default objects
    # Lists, strings, integers, floats, Booleans, None, and dictionaries

    #name_list = ["John", "Richard", "Adam"] # Make list
    #json_names = json.dumps(name_list) # Convert to string
    #print(json_names)
    #jsonfile.write(json_names)

    pancake = dog("Malchi", 10, "White", "Pancake")

    #If we want to serialize, turn into dictionary
    jsonfile.write(json.dumps(pancake.__dict__))

# Reading json from an existing file

with open("./AdamYeisley/ellie.json", "r") as ellie:
    ellie = json.load(ellie)
    print(ellie)