def hero_powers(**kwargs):
    return kwargs

heroes = hero_powers(captain_america="super strength", iron_man="intelligence", spider_man="agility") 
print(heroes)


def greeting(**kwargs):
    if "Thor" in kwargs and kwargs["Thor"] == "powerful":
        return "strongest Avenger"
    elif "Thor" in kwargs:
        return f"{kwargs['Thor']} Thor!"

    return "who is this?"

print(greeting(Thor="powerful"))