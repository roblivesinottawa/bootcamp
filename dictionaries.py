marvel = {
    "name": "Iron Man",
    "power": "high-tech suit",
    "main_skill": "intelligence",
    "status": "alive",
}
for k, v in marvel.items():
    print(v)


dc = dict(name="Batman", age="unknown", main_skill="intelligence", status="unknown")
print(dc.get("rich"))


artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f'{artist["first"]} {artist["last"]}'
print(full_name)


donations = dict(sam=25, lena=88, chuck=13, stan=150)
total_donations = 0
for v in donations.values():
    total_donations += v

print(total_donations)

total_donations = sum(donation for donation in donations.values())
print(total_donations)




from random import choice

food = choice(['pizza', 'quiche', 'tea cake', 'gummy bear'])

bakery_stock = {
    "almond croissant": 12,
    'toffee cookie': 3,
    'morning bun': 1,
    'chocolate chunk cookie': 9,
    'tea cake': 25
}

if food in bakery_stock:
    print(f"{bakery_stock[food]} left of {food}")
else:
    print("we don't make that")



new_user = {}.fromkeys(['name', 'age', 'job', 'email'], 'John')
print(new_user) 

game_properties = ["current_score", "high_score", "number_of_lives", "power-ups", "enemies_on_screen", "enemy_kills"]

initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

inventory = dict(croissant=19, bagel=4, muffin=8, cake=1)
# make a copy of inventory
stock_list = inventory.copy()
# add value 18 to the stock_list under key "cookie"
stock_list["cookie"] = 18
# remove cake from stock_list 
stock_list.pop("cake")

print(stock_list)