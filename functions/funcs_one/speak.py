# this is the one I did by following the instructions

# def speak(animal):
#     if animal == 'pig':
#         return 'oink'
#     elif animal == 'duck':
#         return 'quack'
#     elif animal == 'cat':
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     elif animal != ["pig", "duck", "cat", "dog"]:
#         return "?"
#     else:
#         return "woof"


# refactored version

# by setting "dog as the default parameter, if the user types something other than the given options,
# it will return 'dog' "
# def speak(animal="dog"):
#     if animal == 'pig':
#         return 'oink'
#     elif animal == 'duck':
#         return 'quack'
#     elif animal == 'cat':
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"


# let user select an animal
# animal_input = input("choose an animal: ")
# print(speak(animal_input))


# a refactored version using a dictionary
# noises = dict(dog="woof", pig="oink", duck="quack", cat="meow")

# def speak(animal="dog"):
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

# animal_choice = input("choose an animal: ")
# print(speak(animal_choice))


# another refactoring
def speaking(animal="dog"):
    noises = dict(pig="oink", duck="quack", cat="meow", dog="woof")
    return noises.get(animal, "?")

choose_animal = input("choose animal: ")
print(speaking(choose_animal))