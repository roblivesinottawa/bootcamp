import random

def number_compare(n1, n2):
    if n1 > n2:
        return f"First ({n1}) is greater than second ({n2})"
    elif n2 > n1:
        return f"Second ({n2}) is greater than first ({n1})"
    return "Numbers are equal"

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print(number_compare(number1, number2))