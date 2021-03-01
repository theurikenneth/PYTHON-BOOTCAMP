# automate the grading system to ensure that it uses a for loop to ask for the five subjects marks
# student details
studentName = input("Enter your name\n:")
studentClass = input("Enter your class\n:")
studentClassTeacher = input("Enter your class teacher\n:")

# student grades
#scores per subject
totalScore = 0
subjects = ["math", "Eng", "Kiswahili", "Science", "Social Studies"]
for i in range(len(subjects)):
  
   marks = int(input("What is your" +" "+ subjects[i] +" "+"score:\n"))
   totalScore +=marks

"""studentGrades = int(input("Enter your Maths Grade\n:")), int(input("Enter your English Grade\n:")), int(input("Enter your Kiswahili Grade\n:")), int(input("Enter your Science Grade\n:")), int(input("Enter your SST Grade\n:"))
print(type(studentGrades))
totalScore = 0
for grades in studentGrades:
    totalScore+=grades"""
averageScore = totalScore/5
print("Your name is",studentName)
print("Your class is",studentClass)
print("Your class teacher is",studentClassTeacher)
print("Your total score is",totalScore)
print("Your average score is",averageScore)

if (averageScore>=80.0 and averageScore<=100.0):
    print("Your grade is A")
elif (averageScore>=75.0 and averageScore<=79.9):
    print("Your grade is A-")
elif (averageScore>=70.0 and averageScore<=74.9):
    print("Your grade is B+")
elif (averageScore>=65.0 and averageScore<=69.9):
    print("Your grade is B")
elif (averageScore>=60.0 and averageScore<=64.9):
    print("Your grade is B-")
elif (averageScore>=55.0 and averageScore<=59.9):
    print("Your grade is C+")
elif (averageScore>=50.0 and averageScore<=54.9):
    print("Your grade is C")
elif (averageScore>=45.0 and averageScore<=49.9):
    print("Your grade is C-")
elif (averageScore>=40.0 and averageScore<=44.9):
    print("Your grade is D+")
elif (averageScore>=35.0 and averageScore<=39.9):
    print("Your grade is D")
elif (averageScore>=30.0 and averageScore<=34.9):
    print("Your grade is D-")
elif (averageScore>=0.0 and averageScore<=29.9):
    print("Your grade is E")
else:
    print(f"{averageScore} - Your average score is Invalid!!")
