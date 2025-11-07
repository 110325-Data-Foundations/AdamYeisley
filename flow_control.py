
#Flow Control in Python

# For
# While
# Do-While
# If-else
# Switch
# Try-except (more exception handling)

# For Loops

# For loops iterate through a collection
# For x in collection, execute some code

class_pets = ["Bentley, Tarzan, Puhcat"]

for pet in class_pets:
    print (pet)

for i in range(0,10):
    print (i)

for i in range(0,6):
    if i == 0:
     break
else:
    print("If completed")

# While
count = 0
while(count<5):
   print("From the while loop")
   count += 1 # SHort hand for count = count + 1

# If we need to, we can nest loops, and miox and match them
# If you find yourself 3 or more loops deep... there is probably a better way

# If-else
# We check a condition and if it is truem run block code
# Otherwise, run the else code
# ELif can be repeated indefinitely
# Final else is optional
condition = True
if condition:
   print("If Code")
elif condition:
   print("Elif code")
else:
   print("Else Code")

#Match-case: In other languages this is called switch. New to Python 3.10

print("Please enter a selection (1-3): ")
choice = input()

match choice:
   case "1":
      print("Case 1")
   case "2":
      print("Case 2")
   case "3":
      print("Case 3")
   case _: # Default case, if non above match
      print("Default Case")
