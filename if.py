"""
syntax for the if statement

if expression:
    statement(s)

"""
# if the expression is true, the print will be outputed
# if the expression is false, nothing will be printed
if 10>2:
    print("10 is greater than two")
    name = input("Enter your name:")
    print(name)

""" 
create an application that checks if a number is positive

exception handling in python
"""
n = int(input("Enter a number\n:"))

if n>0:
    print(n,"is positive")
elif n==0:
    print("the number is zero")
else:
    print(f"{n} is negative")

