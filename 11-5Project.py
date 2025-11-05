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
  while True:
   print("Please enter grades or enter a number greater than 100 to exit:")
   grade_entry_input = int(input())
   if grade_entry_input > 100:
     break
   else:
    grade_list.append(grade_entry_input)
 elif mainmenu_input == 3:
  grade_avg = sum(grade_list)/len(grade_list)
  print(grade_avg) 
 elif mainmenu_input == 4:
  print(f"Your name is: " + name)
  print(f"Your grades are: " + str(grade_list))
  print(f"Your grade average is: " + str(grade_avg))
 elif mainmenu_input == 5:
  print("Thanks for using Adam's Grade Calculator! Goodbye.")
  break
 else:
  print("The number entered is not a menu option. Try again.")
  
