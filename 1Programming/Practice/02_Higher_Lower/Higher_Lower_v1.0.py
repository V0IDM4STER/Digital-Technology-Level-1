# Higher Lower Game - Version 1.0

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
                print(error)
                continue
            
            # Checks that response is not too high
            if high is not None and response > high:
                print(error)
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
keep_going = ""
while keep_going == "":
    
    # Get the lowest number, highest number, and  number of rounds
    lowest = intcheck("Lowest Number: ")
    print()
    highest = intcheck("Highest Number: ", lowest + 1)
    print() 
    rounds = intcheck("Number of Rounds: ", 1)

    # Get maximum number of guesses
    range = highest - lowest + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print()
    print("Max Guesses: {}".format(max_guesses))
    print()
    
    guesses_allowed = max_guesses
    rounds_played = 0 
    num_won = 0
    game_stats = []

    while rounds_played < rounds:

        secret = random.randint(lowest, highest)

        guess = ""
        guesses_left = guesses_allowed
        already_guessed = []

        hl_statement("### Round {} ###".format(rounds_played + 1), "#")

        while guess != secret and guesses_left >= 1:

            guess = intcheck("Guess: ", lowest, highest)

            if guess in already_guessed:
                hl_statement("!! You already guessed that number. Please try again.  |  Guesses Left: {} !!".format(guesses_left), "!")
                continue

            guesses_left -= 1
            already_guessed.append(guess)

            if guesses_left >= 1:

                if guess < secret: 
                    hl_statement("^^ Too low, try a higher number.  |  Guesses Left: {} ^^".format(guesses_left), "^")
                
                elif guess > secret:
                    hl_statement("vv Too high, try a lower number.  |  Guesses Left: {} vv".format(guesses_left), "v")

            else:
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")

        if guess == secret:
            if guesses_left == guesses_allowed - 1:
                print("Amazing! You got it in one guess!")
            else:
                print("Well done. You got it in {} guesses.".format(guesses_allowed - guesses_left))
            num_won += 1
        else:
            print("Sorry - you lose this round because you have no guesses left.")
            guesses_left -= 1 # Penalty point for losing

        game_stats.append(guesses_allowed - guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))           # \t means tab
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

    print()
    keep_going = input("Press <enter> to play again or a letter to quit. ")
    print()

print("Thank you for playing!")