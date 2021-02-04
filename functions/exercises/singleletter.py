# function takes a word and a letter as a parameter
def single_letter_count(word, letter):
    # check how many times a certain letter is in that word
    return word.lower().count(letter.lower())
# it will return 0 if no word is found

w = input("please enter a word: ")
l = input("please enter a letter: ")

print(single_letter_count(w, l))