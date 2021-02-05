import string

def capitalize(word):
    return string.capwords(word)

print(capitalize("robson trajano"))


def capitalize1(word):
    return word[:1].upper() + word[1:]

print(capitalize1("robson trajano"))