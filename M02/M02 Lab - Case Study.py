Last_Name = input("Enter your last name: ")
if Last_Name == "ZZZ":
          exit()

if Last_Name == int:
       exit()
        
#This checks the program for special characters
import string 
x = Last_Name
invalidcharacters= set(string.punctuation)
if any(char in invalidcharacters for char in x):
    print("ERROR ! NO SPECIAL CHARACTERS.")
    exit()


First_Name = input("Enter your first name: ")

#This checks the program for special characters
import string 
x = First_Name
invalidcharacters= set(string.punctuation)
if any(char in invalidcharacters for char in x):
    print("ERROR ! NO SPECIAL CHARACTERS.")
    exit()

Student_GPA = float(input("Enter your GPA: "))

print(Last_Name,",", First_Name)

if Student_GPA >= 3.5:
        print("Congratulations! You've made the Deans list")
else: print("You do not meet the necessary requirements to make the Deans list.")

if Student_GPA >= 3.25: 
        print ("Congratulations! You've made the Honor Roll")
else: print("You do not meet the necessary requirements to make the Honor Roll.")

