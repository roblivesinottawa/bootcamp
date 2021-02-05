def generate_odds():
    return [num for num in range(1, 50) if num % 2 != 0]

print(generate_odds())


def odds():
    result = []
    for n in range(1, 50):
        if n % 2 != 0:
            result.append(n)
    return result

print(odds())