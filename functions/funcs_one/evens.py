def return_evens():
    result = []
    for n in range(1, 50):
        if n % 2 == 0:
            result.append(n)
    return result

print(return_evens())

def generate_evens():
    return [n for n in range(1, 50) if n % 2 == 0 ]

print(generate_evens())