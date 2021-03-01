# A tuple is created using ()
# difference between list and tuple is that, tuple is immutable.

dow = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

c = ("mon",[1,2,3],("Hello","World"))

#You can create a tuple in a list

#creating a tuple without ()

moy = "Jan", "Feb", "March", "April"
print(type(moy))

print(moy[:2]) # prints Jan and Feb

t = ("Mark",)
print(type(t))
t = "Mark",   # the comma makes the string a tuple
print(type(t))

a = ["d","asd","asd", [2,3,4,5]]
r,t,y,u = a
print(u)

# index a tuple
# slice a tuple - both +ve and -ve
# slice with step

# Tuple cannot be changed although they can be manipulated,

