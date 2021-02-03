from random import randint

player_wins = 0 
computer_wins = 0
winning_score = 3


def display_header():
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

def pick_computer_move():
    random_num = randint(0, 2)
    if (random_num == 0):
        move = "rock"
    elif (random_num == 1):
        move = "paper"
    else:
        move = "scissors"
    print(f"The computer plays: {move}")
    return move


def calculate_winner(player, computer):
    # use global keyword to access variables located outside of the function
    global player_wins
    global computer_wins
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

def start_game(winning_score):
    while player_wins < winning_score and computer_wins < winning_score:
        # call function while condition true, that will kick off game
        display_header()

        player = input("(enter your choice): ").lower()
        if player == "quit" or player == "q":
            break

        computer = pick_computer_move()
        calculate_winner(player, computer)

def display_winner():
    if player_wins > computer_wins:
        print("CONGRATS, YOU WON!")
    elif player_wins == computer_wins:
        print("IT'S A TIE")
    else: 
        print("OH NO :( THE COMPUTER WON...")

start_game(3)
display_winner()
