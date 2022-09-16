# Lucky Unicorn Full Working Product Version 1
# Program should work - needs to be tested for usability

import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter a number between {} and {}.".format(low, high)

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)
            print()

# Main Routine
# Ask user how much they want to play with (min $1, max $10)

balance = intcheck("How much money would you like to play with? $", 1, 10)

keep_going = ""
while keep_going == "":

    # Token List (Multiple horses, zebras, etc. to prevent unicorn from being chosen too much)
    tokens = ["horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey", "unicorn"]

    # Choose a random token from the list and let the user know what it was 
    token = random.choice(tokens)
    print()
    print("You got a {}.".format(token))

    # Adjust balance correctly for given token
    if token == "unicorn":
        balance += 5
        feedback = "Congratulations! You got a lucky unicorn and have won $5.00."
    elif token == "donkey":
        balance -= 1
        feedback = "Sorry, you didn't win anything this round."
    else:
        balance -= 0.5
        feedback = "Congratulations! You won 50c."

    print()

    # Tell the user how much they won and the amount of money they have left
    print(feedback)
    print("You have ${:.2f} to play with.".format(balance))

    # If the user has enough money to continue, ask if they want to keep playing
    if balance < 1:
        print("Sorry, you don't have enough money to continue.")
        print()
        print("Game Over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to continue playing or any other key to quit.")

# Thank the users for playing when they stop playing
print()
print("Thank you for playing.")
print()
