# numbers = {
#     "first": 1,
#     "second": 2,
#     "third": 3,
# }

# squared_nums = {k: v ** 2 for k, v in numbers.items()}
# print(squared_nums)

stringone = "ABCDE"
stringtwo = "12345"
combined = {stringone[i] : stringtwo[i]for i in range(0, len(stringone))}
combined = list(zip(stringone, stringtwo))
print(combined)

# person = dict(name="John", lastname="Marston")
# capitalized = {k.upper() : v.upper() for k, v in person.items()}
# print(capitalized)

# *************************************************************
# num_list = [1,2,3,4,5,6,7,8,9]
# answer = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
# print(answer)

# *************************************************************
# listone = ["BC", "ON", "MB"]
# listtwo = ["British Columbia", "Ontario", "Manitoba"]
# comb1 = {listone[x] : listtwo[x] for x in range(0, len(listone))}
# comb = dict(zip(listone, listtwo))
# print(comb1)
# print(comb)

# ***************************************************************
person = [['name', 'Jared'], ['job', 'musician'], ['city', 'Toronto']]

answer1 = {p[0] : p[1] for p in person}
print(answer1)

answer2 = dict(person)
print(answer2)

answer3 = {key:value for key, value in person}
print(answer3)


# *************************************************************
answer4 = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
answer5 = {char : 0 for char in "aeiou"}
answer6 = dict.fromkeys("aeiou", 0)

print(answer4)
print(answer5)
print(answer6)