# def is_palindrome(word):
#     for i in range(0, int(len(word) / 2)):
#         if word[i] != word[len(word) - i - 1]:
#             return False
#     return True


def is_palindrome(word):
    return word == word[::-1]

user_input = input("enter a word to check if it's palindrome: ")
print(is_palindrome(user_input))