from random import randint


number = randint(1, 10)

while True:
    guess = int(input("guess the number: >>> "))
    if guess > 10 or guess < 1:
        print("error")
    else:
        print("success")
        play_again = input("do you want to play again? (y/n) ")
        if play_again == "y":
            number = randint(1, 10)
            guess = None
        else:
            print("thanks for playing.")
            break







































        
        