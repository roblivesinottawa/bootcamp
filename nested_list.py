_list  = [[1,2,3], [4,5,6]]
# print(_list[-1][0])

for value in _list:
    for val in value:
        print(val)


coordinates = [[1000.1, 23902],[12342, 67394], [23421, 78943]]

# for location in coordinates:
#     for loc in location:
#         print(loc)

[[print(loc) for loc in location] for location in coordinates]

# failed attempt to emulate code below
# x = []
# o = []
# for val in range(1,4):
#     for num in range(1, 4):
#         if num % 2 != 0:
#            x.append("X")
#         else:
#             o.append("O")
# print(x, o)

# var = [["x" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
# print(var)


# answer = [[x for x in range(1,3)] for num in range(1,3)]
# print(answer)


answer = [[x for x in range(0, 10)] for value in range(0, 10)]
print(answer)


