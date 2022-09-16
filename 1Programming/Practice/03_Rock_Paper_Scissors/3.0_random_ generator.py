# RPS Component 2
# Random Answer Generator

# Imports the random module
import random

# Sets up the choices for the computer
rps = ["rock", "paper", "scissors"]

# Loops following code 10 times
for item in range(0,10):
    # Chooses a random option from the list
    computer = random.choice(rps)
    # Prints it out
    print(computer)