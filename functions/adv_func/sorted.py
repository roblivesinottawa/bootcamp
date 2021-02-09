nums = [4, 9, 40, 23, 98, 1, 90]
print(sorted(nums, reverse=True))


users = [
    {"username": "Jeff", "id": 1},
    {"username": "John", "id": 2},
    {"username": "Mary", "id": 3},
    {"username": "Vick", "id": 4},
    {"username": "Steph", "id": 5},
]

get_names = sorted(users, key=lambda user: user['id'])
print(get_names)

