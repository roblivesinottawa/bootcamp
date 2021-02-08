names = ["Captain America", "Iron Man", "Spider Man", "Thor", "Hulk"]

favourite_avenger = list(map(lambda name: f"the best avenger is {name}",
filter(lambda value: len(value) > 10, names)))

print(favourite_avenger)



names = ["Captain America", "Iron Man", "Spider Man", "Thor", "Hulk"]

def favourite():
    return [f"the best avenger is {name}" for name in names if len(name) > 10]

print(favourite())



heroes = ["Captain America", "Iron Man", "Spider Man", "Thor", "Hulk"]

def hero():
    best_hero = []
    for hero in heroes:
        if len(hero) > 10:
            best_hero.append(hero)
            print(f"the best avenger is {best_hero}")
           


hero()