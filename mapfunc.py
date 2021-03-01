list1 = [1,2,3,4]

# map(function, list) -> takes in two elements: function,list
new_list = list(map(lambda number: number*2, list1))
print(new_list)

list2 = [1, -1, 2, 3, 4, -3, -4, -5, -6]

negative_nums = list(filter(lambda number: number<0,list2))
print(negative_nums)

ls = [1,2,3,4,5]
print(sum(ls))

from functools import reduce
ls = [1,2,3,4,5]
# reduce applies a rolling computation
product = reduce(lambda a,b: a*b, ls)

print(product)

from functools import reduce
ls = [1,2,3,4,5]
# reduce applies a rolling computation
product = reduce(lambda a,b: a+b, ls)

print(product)