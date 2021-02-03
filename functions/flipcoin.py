from random import random

def flip_coin():
    num = random()
    if num > 0.5:
        return f"HEADS = {num}"
    else:
        return f"TAILS  = {num}"

print(flip_coin())