# Lucky Unicorn Full Working Product Version 1
# Program should work - needs to be tested for usability

# Imports
from os import stat
import random

# Functions

# Integer checking function.
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter a number between {} and {}.".format(low, high)

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print()
                print(error)
                print()
        
        except ValueError:
            print()
            print(error)
            print()

# Function to print out 'token statements'. Takes message and applies decoration to top and bottom of the message based on the kind of token.
def token_statement(statement, char):
    print()
    print(char*len(statement))
    print()
    print(statement)
    print()
    print(char*len(statement))

# Main Routine

# Cost and Payout Constants
COST = 1
UNICORN = 5
ZEBRA_HORSE = 0.5
DONKEY = 0

# Introduction / Instructions
print()
print("**** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 and press <enter>. (Whole dollars only).")
print()
print("- It costs ${:.2f} per round. -".format(COST))
print()
print("~ Payouts ~")
print(" - Unicorn = ${:.2f}".format(UNICORN))
print(" - Zebra or Horse = ${:.2f}".format(ZEBRA_HORSE))
print(" - Donkey = ${:.2f}".format(DONKEY))
print()
print()

# Ask user how much they want to play with (min $1, max $10).

balance = intcheck("How much money would you like to play with? $", 1, 10)
round_count = 0 # Variable to count number of rounds.

keep_going = ""
while keep_going == "":

    # Token List (Multiple horses, zebras, etc. to prevent unicorn from being chosen too much).
    tokens = ["horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey", "unicorn"]

    # Choose a random token from the list and add 1 to the number of rounds played.
    token = random.choice(tokens)
    round_count += 1

    # Give feedback and adjust balance correctly for given token.
    if token == "unicorn":
        balance += UNICORN
        token_statement("**** Congratulations! You got a lucky unicorn and have won ${:.2f}. ****".format(UNICORN), "*")
    elif token == "donkey":
        balance -= COST
        token_statement("==== Sorry, you got a {} didn't win anything this round. ====".format(token), "=")
    else:
        balance -= ZEBRA_HORSE
        token_statement("<<< Good try. You got a {} and won back ${:.2f}. >>>".format(token, ZEBRA_HORSE), "^")

    print()

    # If the user has enough money to continue tell them the amount of money they have left and how many rounds they've played.
    # If the user doesn't have enough money to continue, tell them and say game over.
    if balance >= 1:
        print("You have ${:.2f} to play with.".format(balance))
        print()
        print("Rounds Played: {}".format(round_count))
        print()
        keep_going = input("Press <enter> to continue playing or a letter and then <enter> to quit.")
    else:
        print("Sorry, you don't have enough money to continue.")
        print()
        print("Game Over")
        keep_going = "end"

# Thank the users for playing when they stop playing
print()
print("Thank you for playing.")
print()