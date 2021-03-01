"""
x = [1,2,3,4]

new_list = []

for each in x:
    new_list.append(each *2)

print(new_list)
"""

"""
The above can be done using list comprehension

syntax

[expression for var in it]

where it can be a list or a string
"""

list1 = [1,2,3,4]
new_list = [x for x in list1]
print(new_list)

new_list = [x-1 for x in list1]
print(new_list)

new_list = [x*2 for x in list1]
print(new_list)

name = "techcamp" #['t','e']
name_list = []
for i in name:
    name_list.append(i)
print(name_list)

name = "techcamp"
name_list = [char for char in name]
print(name_list)

"""
construct list comprehensions that have conditional statements
"""

# case study 1: Generate a list of all even numbers from 1-10
even_numbers_list = []
for each in range(1,11):
    if each % 2 == 0:
        even_numbers_list.append(each)

print(even_numbers_list)

even_numbers_list = [num for num in range(1,11) if num % 2 == 0 ]
print(even_numbers_list)

# case study 2: Generate a list of all odd numbers from 90-100
odd_numbers_list = [num for num in range(90,100) if num % 2 == 1 ]
print(odd_numbers_list)

list2 = [x*2 if x%2 == 0 else x*3 for x in range(1,11)]
print(list2)