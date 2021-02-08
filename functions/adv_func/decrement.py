# this way:

decrement_list = list(map(lambda x: x - 1, [19,22,38]))
print(decrement_list)


# or 

def decrement(list_nums):
    return list(map(lambda num: num - 1, list_nums))

print(decrement([2,3,4]))