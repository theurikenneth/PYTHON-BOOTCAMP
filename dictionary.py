# dictionary - it is unordered collection of items
# data in a dictionar is stored in key/value pairs
# keys should be unique and should be immutable data type
# values can be of any data type
# to access a value in a dictionary, you need to call the key.

# how to create a dictionary
# use {} or dict() function

my_details = {
    "first_name":"Kenneth",
    "last_name":"Ken",
    True:"it is true",
    10:"Ten",
    "interests":["cooking","fishing"],
    "isHappy":False,
    "parents":{
        "mother":{
            "fName":"Jane",
            "lName":"Doe",
            "age":24
        },
        "father":{
            "fName":"John",
            "lName":"Kamau",
            "age":24
        },
    }
}

print(my_details["first_name"])
print(my_details["interests"])
print(my_details["parents"]["mother"])
#to change mother's name first name
my_details["parents"]["mother"]["fName"] = "Joyce",
print(my_details["parents"]["mother"])

# cop, pop, clear

# dictionary comprehension

# input

print(type(my_details))