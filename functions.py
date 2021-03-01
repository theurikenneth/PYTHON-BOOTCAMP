def grade_calc(maths,english,science): # function name
    total=maths+english+science
    return total

print(grade_calc(35,80,100)) # using positional arguments ie. 35 takes position for maths etc
print(grade_calc(maths=35,english=80,science=100)) # using key-word arguments 
print(grade_calc(35,english=80,science=100)) # positional argument cannot come after a ke-word argument

"""
Write a function canner_can that takes a single argument item in the form of a 
string, and returns the string 'Can you can a [STRING] as a canner can can a can?', 
where '[STRING]' takes the value of item.
"""
def canner_can(item):
    return f"Can you can a {item} as a canner can can a can?"

print(canner_can("blahblah"))
print(canner_can("yellow"))

#Define function that calculates the number of seconds in a year.
def seconds_calculator(days=365):   
    return days*24*60*60

print(seconds_calculator()) # the unknown of days is already defined 
print(seconds_calculator(364))

"""
define a function which finds the maximum number among three numbers:
"""
def max_number(a,b,c):
    my_list = [a,b,c]
    my_list.sort()
    return my_list[-1]

print(max_number(64,42,48))

def maximum(a, b, c): 
  
    if (a >= b) and (a >= c): 
        largest = a 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c   
    return largest 

print(maximum(10,36,21))