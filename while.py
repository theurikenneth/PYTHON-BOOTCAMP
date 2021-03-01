"""
While lopps are used when you don't know the number of 
iterations you intend to make

- While loop executes as long as the test expression evaluates to true
- After each iteration, the expression is evaluated
- 
"""

#while True:
 #   print("its true") # The code runs and never stops

i = 1
while i<=10:
    print(i)
    i+=1

i = 10
whileSum=0
while i>=1:
    print(i)
    whileSum+=i
    i-=1
print("The sum is",whileSum)

i=10
whileSum=0
while i<=10 and i>0:
    print(i)
    whileSum+=i
    i-=1
print("The sum of the numbers is",whileSum)