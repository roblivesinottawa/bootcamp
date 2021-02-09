nums = [2,4,5,6,7,5,4,34,67,87,34]
print(max(nums))
print(min(nums))


names = ["Tony Stark", "Steve Rogers", "Bruce Banner", "Peter Parker"]

max_name = max(names, key=lambda n: len(n))
print(max_name)


songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},

]

print(min(songs, key=lambda song: song['playcount']))
print(max(songs, key=lambda song: song['playcount']))

