def multiple_letter_count(string):
    return {k: string.count(k) for k in string}

print(multiple_letter_count("great"))

