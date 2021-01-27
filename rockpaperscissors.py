from random import randint

# initilize the score for main player and computer
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    # show score
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("rock, paper, scissors game")

    player = input("player 1, please choose 'rock', 'paper' or 'scissors': >>> ").lower()
    if player == "quit" or player == "q":
        break
    random_number = randint(0, 2)
    if random_number == 0:
        computer = "rock"
    elif random_number == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"computer plays {computer}")


    if player == computer:
        print("it's a tie.")
    elif player == "rock":
        if computer == "paper":
            print("computer wins.")
            computer_wins += 1
        else:
            print("player wins.")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins")
            player_wins += 1
        else:
            print("computer wins.")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins.")
            computer_wins += 1
        else:
            print("you win.")
            player_wins += 1
    else:
        print("please enter a valid move.")


if player_wins > computer_wins:
    print("congrats, you're the winner.")
elif player_wins == computer_wins:
    print("it's a tie.")
else:
    print("sorry you lose.")
   