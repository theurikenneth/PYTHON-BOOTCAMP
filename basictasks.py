# SECTION A
# Task 1
"""
Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
Hint: Use input () to get the persons input
"""

stringInput = str(input("Please input a string:\n"))

if stringInput == "yes":
    print("Yes")
elif stringInput == "Yes":
    print("Yes")
elif stringInput == "YES":
    print("Yes")
else:
        print("No")

string = input("Enter a string:")

if string == "yes" or string == "YES" or string == "Yes":
    print("Yes")
else:
    print("No")

# Task 2
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function
"""
a = (5,10,15,20,25,30)
print(a[0],a[len(a)-1])

def mylist4(a):
    return [a[0],a[-1]]
print(mylist4([5, 10, 15, 20, 25]))

# Task 3
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
1.	If the number is a multiple of 4, print out a different message.
"""
num = int(input("Enter a number:\n"))

if num%4==0:
    print("You entered a multiple of 4")
elif num%2==0:
    print("You entered an even number")
else:
    print("You have entered an odd number")

def odd_even(anyNumber):
    if int(anyNumber)%2 == 0:
        print("{} is an even number".format(anyNumber))
        if int(anyNumber)%4 == 0:
            print("{} is a multiple of 4".format(anyNumber))
    else:
        print("{} is an odd number".format(anyNumber))
odd_even(16)
# Task 4
"""
With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.
"""
tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)

def func_tuple(a_tuple):
    midpoint = int(len(a_tuple)/2)
    firsthalf = a_tuple[:midpoint]
    lasthalf = a_tuple[midpoint:]
    fh_str = str(firsthalf)
    lh_str = str(lasthalf)
    print(fh_str)
    print(lh_str)
    a = fh_str.strip('()')
    b = lh_str.strip('()')
    print(a)
    print(b)

func_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Task 5
# Write a program that takes the base and height of a triangle and returns its area.
base = int(input("Enter the base:\n"))
height = int(input("Enter the height:\n"))
area = 0.5*base*height
print("The area of the triangle is",area,"square units")

def triangle_area(base,height):
    return 0.5*base*height
print(triangle_area(3,5))

#Task 6
"""
Given an integer n(use the input() function) perform the following conditional actions:
•	If n is odd, print Weird
•	If n is even and in the inclusive range of 2  to 5 , print Not Weird
•	If n is even and in the inclusive range of 6 to 20, print Weird
•	If n is even and greater than 20, print Not Weird
"""
n = int(input("Enter a number:\n"))

if n%2==1:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")

# SECTION B
# Task 1
"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains a list x of i integers each separated by a space.
"""
n = int(input())

nums = map(int, input().split())    
print(sorted(list(set(nums)))[-2])

list = [2 3 6 6 5]
no_of_students = int(input("Enter number of students:\n"))
scores = input("Enter student scores:\n").split( )[0:no_of_students]# split method splits a string into a list then we slice the list scores to be equivalent to the number of students
new_scores = list(set(scores))#set removes duplicates
new_scores.sort(reverse=True)
print(new_scores[1])

# Task 2
"""
Given the names and grades for each student in a Physics class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""
n = int(input()) # getting test case input

name_list = []
mark_list = []

for i in range(n):
    name_list.append(input()) # getting student name
    mark_list.append(input()) # getting student's mark
set_mark_list = set(mark_list)
min_mark = sorted(set_mark_list)[1:2]
outer_list = []

for name in range(len(name_list)):
    inner_list = []
    inner_list.append(name_list[name])
    inner_list.append(mark_list[name])
    outer_list.append(inner_list)

lowest_number_name_list = []
for i in range(len(outer_list)):
    if mark_list[i] == min_mark[0]:
        lowest_number_name_list.append(name_list[i])
        
sorted_list = sorted(lowest_number_name_list, key=str.lower)
for i in range(len(sorted_list)):
    print(sorted_list[i])

n=int(input())
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x: (x[1],x[0]))
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])    
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x])

# Task 3
"""
HackerLand University has the following grading policy:
Every student receives a  in the inclusive range from  to .Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:
If the difference between the  and the next multiple of  is less than , round up to the next multiple of .If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to but  will not be rounded because the rounding would result in a number that is less than .
Given the initial value of  for each of Sam's students, write code to automate the rounding process.
Function Description
Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.
gradingStudents has the following parameter(s):
grades: an array of integers representing grades before rounding
Input Format
The first line contains a single integer, , the number of students. 
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.
Constraints
Output Format
For each , print the rounded grade on a new line.
"""
def gradingStudents(grades):

    for x,i in enumerate(grades):
        if(i>=38) and (i%5)>=3:
            grades[x]=i+5-(i%5)
    return (grades)


limit=int(input())
arr=[]
for a in range(limit):
	ar = int(input())
	arr.append(ar)
m = []
for i in arr:
	while i%5!=0:
		i+=1
		if i%5==0:
			m.append(i)
new=[]
for k in range(len(m)):
	if m[k]-arr[k]<3:
		new.append(m[k])
	else:
		new.append(arr[k])
print(*new,sep='\n')