# HL Component 5 - No Duplicate Numbers

# To Do
# Set up empty list called already guessed
# When user guesses, add guess to list
# For each guess, check that the number is not already guessed

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))

    # Checks that guess is not already guessed
    if guess in already_guessed:
        print("You have already guessed that number. No guesses will be lost.")
        print("Guesses Left: {}".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

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