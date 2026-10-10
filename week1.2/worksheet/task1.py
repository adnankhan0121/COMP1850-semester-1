# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter your grade: ")
if (grade.isdecimal()):
     grade = int(grade)

     if 0 <= grade <= 100:
          
        if grade >= 70:
          print(f"{grade} is a Distinction")
        elif grade >= 40:
          print(f"{grade} is a Pass")
        else:
          print(f"{grade} is a Fail")
     else:
        print("Error: Grade must be an integer between 0 and 100")
        sys.exit()         
          
          
else:
      print("Error: Grade must be an integer between 0 and 100")
      sys.exit()