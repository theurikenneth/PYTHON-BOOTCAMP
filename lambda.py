"""
keyword: lambda
syntax:
lambda parameter: expression
POINTS TO NOTE:
    * Can have any number of parameters but only one expression
"""
def add_two(num1):
    return num1+2

print(add_two(2))

add_two = lambda num1: num1+3

print(add_two(2))

to_upper = lambda str : str.upper()
print(to_upper("techcamp"))

even_odd = lambda num: "even" if num%2 ==0 else "odd"
print(even_odd(2))

def even_odd(number:int) ->str:
    if number%2 == 0:
        return "even"
    else:
        return "odd"

print(even_odd(2))

def weird_function(number:int, value_to_add:int) ->str:
    """ This function takes two arguments...."""
    return number+value_to_add

print(even_odd(3))
print(weird_function(2,5))

even_odd = lambda num: "even" if num%2==0 else "odd"
weird_function = lambda number, value_to_add: number+value_to_add

print(even_odd(3))
print(weird_function(2,5))


