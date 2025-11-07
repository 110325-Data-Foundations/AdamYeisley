import statistics
print("Welcome to Adam's Grade Calculator!")
grade_list = []
while True:
 print("Welcome to the main menu. Please enter a number and press enter to select a menu option.")
 print("1 - Name Selection")
 print("2 - Grade Entry")
 print("3 - Grade Average")
 print("4 - All Entered Info")
 print("5 - Exit Program")
 mainmenu_input = int(input())

 if mainmenu_input == 1:
  print("Please enter your first name:")
  name = input()

 elif mainmenu_input == 2:
  print("Please enter grade(s) and enter a number outside of 0-100 to exit.")
  while True:
   grade_entry_input = int(input())
   if 0 < grade_entry_input < 100:
     grade_list.append(grade_entry_input)
   else:
    print("You have entered a number outside of the scope of 0-100, returning to main menu.")
    break

 elif mainmenu_input == 3:
  grade_avg = sum(grade_list)/len(grade_list)
  print(grade_avg) 
 elif mainmenu_input == 4:
  print(f"Your name is: " + name)
  print(f"Your grades are: " + str(grade_list))
  print(f"Your grade average is: " + str(grade_avg))
  print(f"Highest grade: " + str(max(grade_list)))
  print(f"Lowest grade: " + str(min(grade_list)))

 elif mainmenu_input == 5:
  print("Thanks for using Adam's Grade Calculator! Goodbye.")
  break
 else:
  print("The number entered is not a menu option. Try again.")
  
