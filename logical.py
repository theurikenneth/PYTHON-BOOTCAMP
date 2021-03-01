"""
logical operator are words or symbols used to connect two or moreexpressions
3 types: and, or, not
return boolean ie. True or False

and - returns True if all expressions evaluate to true
or - returns True if any/either expression evaluates to true
not - returns True if expression is False

e.g. 1
A       and         B
True                True    - True
True                False   - False
False               True    - False
False               False   - False

e.g. 2
A       or        B
True                True    - True
True                False   - True
False               True    - True
False               False   - False

not A - False

"""
print(10>20 and 20>10)
print(10>20 or 20>10)
print(not 10>20)