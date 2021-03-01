"""
REQUIREMENTS - PART A
- CREATE A CONSOLE APP THAT ASKS FOR THE FOLLOWING:
    -STUDENT NAME
    - CLASS
    - CLASS TEACHER
- ASK FOR THE SCORES FOR THE FOLLOWING SUBJECTS:
    1. Math 2. Eng  3. Kisw 4. Sci  5. SST
-COMPUTE THE FOLLOWING
    a) Total score
    b) Average Score
"""

"""# student details
studentName = input("Enter your name\n:")
studentClass = input("Enter your class\n:")
studentClassTeacher = input("Enter your class teacher\n:")

# student grades
mathGrade = int(input("Enter your Maths Grade\n:"))
engGrade = int(input("Enter your English Grade\n:"))
kiswGrade = int(input("Enter your Kiswahili Grade\n:"))
sciGrade = int(input("Enter your Science Grade\n:"))
sstGrade = int(input("Enter your SST Grade\n:"))

# total and average scores
totalScore = mathGrade+engGrade+kiswGrade+sciGrade+sstGrade
averageScore = totalScore/5

print("Your name is",studentName)
print("Your class is",studentClass)
print("Your class teacher is",studentClassTeacher)
print("Your total score, out of 500, is",totalScore)
print("Your average score is",averageScore)
"""

"""
Part B
Using the following grading system, grade the student:
based on the average score
80-100 A
75-79 A-
70-74 B+
65-69 B
60-64 B-
55-59 C+
50-54 C
45-49 C-
40-44 D+
35-39 D
30-34 D-
0-29 E

Anything outside 0 to 100
I - Invalid
"""

# student details
studentName = input("Enter your name\n:")
studentClass = input("Enter your class\n:")
studentClassTeacher = input("Enter your class teacher\n:")

# student grades
mathGrade = int(input("Enter your Maths Grade\n:"))
engGrade = int(input("Enter your English Grade\n:"))
kiswGrade = int(input("Enter your Kiswahili Grade\n:"))
sciGrade = int(input("Enter your Science Grade\n:"))
sstGrade = int(input("Enter your SST Grade\n:"))

# total and average scores
totalScore = mathGrade+engGrade+kiswGrade+sciGrade+sstGrade
averageScore = totalScore/5

print("Your name is",studentName)
print("Your class is",studentClass)
print("Your class teacher is",studentClassTeacher)
print("Your total score is",totalScore)
print("Your average score is",averageScore)

if (averageScore>=80 and averageScore<=100):
    print("Your grade is A")
elif (averageScore>=75 and averageScore<=79):
    print("Your grade is A-")
elif (averageScore>=70 and averageScore<=74):
    print("Your grade is B+")
elif (averageScore>=65 and averageScore<=69):
    print("Your grade is B")
elif (averageScore>=60 and averageScore<=64):
    print("Your grade is B-")
elif (averageScore>=55 and averageScore<=59):
    print("Your grade is C+")
elif (averageScore>=50 and averageScore<=54):
    print("Your grade is C")
elif (averageScore>=45 and averageScore<=49):
    print("Your grade is C-")
elif (averageScore>=40 and averageScore<=44):
    print("Your grade is D+")
elif (averageScore>=35 and averageScore<=39):
    print("Your grade is D")
elif (averageScore>=30 and averageScore<=34):
    print("Your grade is D-")
elif (averageScore>=0 and averageScore<=29):
    print("Your grade is E")
else:
    print(f"{averageScore} - Your average score is Invalid!!")


try:
    x = int(input("Enter a number\n:"))
    print(x)
    except Exception as e:
        # print(e)
        print("Ensure you type an integer")

# raise keyword
# assertion

assert 10!=10