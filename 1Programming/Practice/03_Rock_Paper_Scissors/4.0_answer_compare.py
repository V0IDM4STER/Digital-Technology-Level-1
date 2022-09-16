# RPS Component 3
# Compare User to Computer

import random

# Sets up the choices for the computer
rps = ["rock", "paper", "scissors"]

# Randomly chooses either r, p, or s for the computer
computer = random.choice(rps)

PLAYER = "s" # Replace with answer checker in due course

# Sees what the player chose and decides who won/lost/tied
if PLAYER == "rock" or PLAYER == "r":
    print(computer)
    if computer == "rock":
        print("Tie")
    elif computer == "paper":
        print("You Lose")
    else: 
        print("You Win")

elif PLAYER == "paper" or PLAYER == "p":
    print(computer)
    if computer == "rock":
        print("You Win")
    elif computer == "paper":
        print("Tie")
    else:
        print("You Lose")

elif PLAYER == "scissors" or PLAYER == "s":
    print(computer)
    if computer == "rock":
        print("You Lose")
    elif computer == "paper":
        print("You Win")
    else:
        print("Tie")