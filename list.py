# Python Lists
"""
Lists - sequence used for storing possibly different objects
    * Lists are defined by [] with each entr separated by a comma
    * Each entry in a list is called an element
    * sequences -> string, list, tuple
"""

#creating a list of strings
names = ["Daniel", "Janet", "Kevin", "Nelly", "Kenneth"]
print(type(names))
# list of ints
scores = [90,70,80]
#list of float
weights = [11.2,33.5,17.8]
#list of bools
status = [True, True, False, False]
#mixed list
x = [True, "Mark",90.8,17.2,12,False,True]
# nested list-list inside a list
y = [10.2, "Brian", names]

print(y)
"""
How to access elements inside a list
* Use list indexing - [x] - where x is the index of the element
"""
# print Nelly from names list
print(names[3])
print(names[-2])

z = [[12,23,[18,True,"8080",["Jane","Mary"],"Hello"]],"Ken",False,[7,10.2]]
# print 23
print(z[0][1])
# print ["Jane","Mary"]
print(z[0][2][3])
# print False
print(z[2])
# print "Hello"
print(z[0][2][4])
# print [18,True,"8080",["Jane","Mary"],"Hello"]
print(z[0][2])
# print 10.2
print(z[3][1])
# check the length of your string
print(len(z))

# check the length of the string "Mary"
print(len(z[0][2][3][1]))

h = [True,"20", [18.7,[["Yeah", False], ["Ahah", 19, 90,2]], "Red", "Yellow", 10]]
# Print False
print(h[2][1][0][1])
# Print "Ahah"
print(h[2][1][1][0])

# list slicing - it is obtaining a range of elements in a list
cars = ["subaru","Toyota","Mazda","premio","pajero"]
print (cars[2:]) # prints "Mazda","premio","pajero"

# slicing with step
print(cars[::2]) #prints subaru, mazda and pajero

# lists are mutable
# 1. use of assignment operator using =
# to change subaru to 100 in the string cars
cars[0] = 100
print(cars)
# to modify pajero to 20
cars[-1] = 20
print(cars)

#2. use the append() method
cars.append(300)
print(cars) # adds 300 after 20

# research 1 on list manipulation methods
#3. pop(), remove(), 

#remove element from list
# to remove toyota
del cars[1]
print(cars)

x = [1,2,3]
y = [4,5,6]
z = x+y
print(z)

# to insert at a specific point
z.insert(3, "Ken")
print(z)

# research 2 list comprehension

# membership operator
# to check if 7 is in z
print(7 in z) # Gives False
print(7 not in z) # Gives True

# research 3 ORM



