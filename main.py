import random
def get_choices():
    player_choice = input("ENTER A CHOICE(ROCK,PAPER,SCISSORS): ")
    options = ["rock", "paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player,computer):
    print("you chose "+ player , " computer chose " +computer )
    if player == computer:
        print("its a tie!!")
    elif player == "rock":
        if computer == "scissors":
            print("you win")
        else: print("you lose")
    elif player == "scissors":
        if computer == "rock":
            print("you lose")
        else: print("you win")
    elif player == "paper":
        if computer == "rock":
            print("you winnn")
        else: computer == "scissors"
        print("you lose")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])


