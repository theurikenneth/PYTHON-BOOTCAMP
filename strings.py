"""
string - anything wrapped in either single or double quotes
"""

firstName = 'Kenneth'
lastName = "Ken"

print(type(firstName))
print(type(lastName))
"""
How to get a character from a string
This is called string indexing ->
NB: Indexing starts from 0
to index, use [x] where x is the index you want to get
"""

# example 1 - Positive indexing
print (firstName[0])
# we get letter k
print (firstName[5])
# we get letter t

# example 2 - negative indexing
print(firstName[-7])
# we get letter k

"""
How to get a range of characters from a string
This is called string slicing
to slice, use[x:y:z] where x is starting index and y is the stopping index
NB: y is never included
NB: z represents a step
"""

# example 1 - positive slicing
inst = "techcamp"
print(inst[0:4])
# we get the letters tech
print(inst[4:8])
# we get the letters camp

# example 2 - negative slicing
print(inst[-4:])
# we get the letters camp
print(inst[-8:-4])
#we get the letters tech

# example 3 - slicing with a step
print(inst[::1])
# prints techcamp
print(inst[::2])
# prints tccm
print (inst[::3])
# prints thm

"""
string concatenation
"""

a = "tech"
b = "camp"
c = a + b
fullName = "tech"+"camp"+" Kenya"
# remember space ( ) is a character
print(fullName)

a = "subaru"
b = "TOYOTA"

print(a.upper())
# prints SUBARU
print(b.lower())
# prints toyota
print(a.title())
# prints Subaru
print(a.isupper())
# prints False