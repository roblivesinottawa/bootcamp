# def remove_negatives(num_list):
#     no_negatives = list(filter(lambda num: num >= 0, num_list))
#     return no_negatives


# print(remove_negatives([-2, -4, 8, 7, 3, 0]))


numbers = [-1,-3,-5,6,7,-4,3,10, -34, 43]

remove_negatives = list(filter(lambda n: n >= 0, numbers))
print(remove_negatives)

remove_positives = list(filter(lambda num: num < 0, numbers))
print(remove_positives)