# HL Component 4 - Win-Loss Mechanics

# To Do
# Set up number of guesses
# Count no. of guesses
# If user runs out of guesses print "you lose"
# If user guesses secret number within number of guesses print "well done"

SECRET = 7
GUESSES_ALLOWED = 4

# Initialize variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    # If user has guesses left ...
    if guesses_left >= 1:
        if guess > SECRET:
            print("Too high. Try a lower number.")
            print("Guesses Left: {}".format(guesses_left))

    # If the user is out of guesses
        elif guess < SECRET:
            print("Too low. Try a higher number.")
            print("Guesses Left: {}".format(guesses_left))
    
    else:
        if guess > SECRET:
            print("Too high.")
        elif guess < SECRET:
            print("Too low.")

if guess == SECRET:
    # If the user guessed right the first time
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it right in one guess!")
    else:
        print("Well done! You won in {} guesses.".format(GUESSES_ALLOWED - guesses_left))

# If user has run out of guesses (loses game)
else:
    print("Sorry - you lose this round because you have no guesses left.")