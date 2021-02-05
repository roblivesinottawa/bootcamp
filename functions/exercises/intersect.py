def intersection(listone, listtwo):
    return list(set(listone).intersection(listtwo))
    # return [val for val in set(listone) & set(listtwo)]
    # return [val for val in listone if val in listtwo]


print(intersection([1,2,3], [2,3,4]))
print(intersection(['a', 'b', 'c'], ['c', 'd', 'e']))