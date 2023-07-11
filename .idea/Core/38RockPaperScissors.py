import random

while True:
    choices = ["scissors", "rock", "paper"]

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input("Rock, Paper, or Scissors?: ").lower()



    if player == computer: #Covers all Ties
        print("computer: " + computer)
        print("player: " + player)
        print("tie!")
    elif player == "rock": # Rock beats scissors Player wins
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("player Wins!")
    elif player == "paper": # Rock beats scissors Computer wins
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("player Wins!")
    elif player == "scissors": # Scissors beats paper Player wins
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("player Wins!")
    elif player == "rock": # Paper beats rock Computer wins
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("Computer Wins!")
    elif player == "scissors": #Computer wins
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("Computer Wins!")
    elif player == "paper": #Computer wins
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("player Wins!")

    playAgain = input("Play again? Yes or no?: ").lower()
    if playAgain != "yes":
        break

print("Bye!")
