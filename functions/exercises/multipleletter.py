def multiple_letter_count(string):
    return {k: string.count(k) for k in string}


answer = input("enter a word: ")
print(multiple_letter_count(answer))

