# Higher Lower Game - Version 2.0
# Added an introduction, round limit and more comments

# Imports
import random
import math

# Functions
# Number Checking Function
def intcheck(question, low = None, high = None):

    # Sets up error message
    if low is not None and high is not None:
        error = "Please enter an integer that is between {} and {}. ".format(low, high)
    
    elif low is not None and high is None:
        error = "Please enter an integer that is more than than or equal to {}. ".format(low)
    
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or equal to {}. ".format(high)
    
    else: 
        error = "Please enter an integer. "


    while True:

        try: 
            response = int(input(question))

            # Checks that reponse is not too low
            if low is not None and response < low:
                print()
                print(error)
                print()
                continue
            
            # Checks that response is not too high
            if high is not None and response > high:
                print()
                print(error)
                print()
                continue

            return response
        
        except ValueError: 
            print(error)
            continue

# Statement Generator Function
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Main Routine

# Introduction
print()
print("*** Welcome to the Higher Lower Game ***")
print()
print("This is a game where you try and guess a secret number between two numbers.")
print()
print("The game will generate the secret number from the number between the two numbers you'll be asked to give at the start of the game.")
print()
print("After you give the game the lowest and highest numbers allowed, it'll ask you for the number of rounds you want to play.")
print()
print("After that, the game will tell you the maximum number of guesse you get per round and you can start guessing.")
print()
print("Have fun!")
print()

# Start of game loop
keep_going = ""
while keep_going == "":
    
    # Get the lowest number, highest number, and  number of rounds
    print()
    lowest = intcheck("Lowest Number: ")
    print()
    highest = intcheck("Highest Number: ", lowest + 1)
    print()
    rounds = intcheck("Number of Rounds: ", 1, 100)

    # Get maximum number of guesses
    range = highest - lowest + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print()
    print("Max Guesses: {}".format(max_guesses))
    
    # Set up things for game statistics
    guesses_allowed = max_guesses
    rounds_played = 0 
    num_won = 0
    game_stats = []

    # Start of loop for each round
    while rounds_played < rounds:

        # Generate secret number
        secret = random.randint(lowest, highest)

        # Set up number of guesses and list of numbers already guesses
        guess = ""
        guesses_left = guesses_allowed
        already_guessed = []

        hl_statement("### Round {} ###".format(rounds_played + 1), "#")

        # Loops asking for guess if the guess isn't the secret number and the user has guesses left
        while guess != secret and guesses_left >= 1:

            # Asks for guess
            guess = intcheck("Guess: ", lowest, highest)

            # Checks if the guess is in the list of already guessed numbers
            if guess in already_guessed:
                hl_statement("!! You already guessed that number. Please try again.  |  Guesses Left: {} !!".format(guesses_left), "!")
                continue

            guesses_left -= 1
            already_guessed.append(guess)

            # Gives feedback based on guess
            if guesses_left >= 1:

                if guess < secret: 
                    hl_statement("^^ Too low, try a higher number.  |  Guesses Left: {} ^^".format(guesses_left), "^")
                
                elif guess > secret:
                    hl_statement("vv Too high, try a lower number.  |  Guesses Left: {} vv".format(guesses_left), "v")

            else:
                if guess < secret:
                    print("Too low!  |  No Guesses Left")
                elif guess > secret:
                    print("Too high!  |  No Guesses Left")

        # Gives feedback based on when the user got the guess right
        if guess == secret:
            if guesses_left == guesses_allowed - 1:
                print("Amazing! You got it in one guess!")
            else:
                print()
                print("Well done. You got it in {} guesses.".format(guesses_allowed - guesses_left))
                print()
            num_won += 1
        else:
            print()
            print("Sorry - you lose this round.")
            print()

        game_stats.append(guesses_allowed - guesses_left)
        # Tell user how many rounds they've won or lost this game
        print("Won: {}   |   Lost: {}".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

    # Print each round's outcome
    print()
    print("*** Game Scores ***")
    list_count = 1
    for item in game_stats:

        # Indicates if game has been won or lost
        if item > guesses_allowed:
            status = "lost, ran out of guesses"
        else:
            status = "won"
        
        print("Round {}: {} ({})".format(list_count, item, status))
        list_count += 1

    # Calculate game statistics then print them
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats)/len(game_stats)

    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    # Ask user if they want to play again
    print()
    keep_going = input("Press <enter> to play again or a letter to quit. ")
    print()

# If not thank the user for playing and end the game
print("Thank you for playing!")