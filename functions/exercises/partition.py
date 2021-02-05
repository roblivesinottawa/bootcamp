# def partition(_list, callback):
#     truthy = []
#     falsy = []
#     for i in _list:
#         if callback(i):
#             truthy.append(i)
#         else:
#             falsy.append(i)
#     return [truthy, falsy]

# def isEven(num):
#     return num % 2 == 0

# #####################################################################
def partition(lst, func):
    return [[val for val in lst if func(val)], [val for val in lst if not func(val)]]

def isOdd(n):
    return n % 2 != 0

answer = partition([1,2,3,4], func=isOdd)
print(answer)

# ########################################################################


