"""
why for loop?
    - repeat a block of code severally
    - in python, for loop to iterate over seqeunces
    - what is sequence? include string, tuple, dict, list

    syntax:

        for variable in sequence:
            //valid python statement(s)
    for loops while iterating over a sequence will only terminate when the last element is reached

"""

ls =  [10,20,30,40]
print(ls[0])
print(ls[1])
print(ls[2])
print(ls[3])

for element in ls:
    print(element)
    pass

for char in "techcamp":
    print(char)
    pass

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

for each in student:
    print(each,student[each])

for k,v in student.items():
    print(k,v)

for k in student.items():
    print(k)

for number in range(1,11):
    print(number)
