def count_sevens(*args):
    return args.count(7)

nums = [23,4,5,63,224,68,7,56,79,7,43,56,7,54,23,5,67,7,8,9,4,3,7,9,3,7,8,7,76,34,67,89,9,76,5,4,6,8,7,6,5,4,3,3,2]

result = count_sevens(1,4,7,5,4,3,2,6,7)
print(result)
result1 = count_sevens(*nums)
print(result1)