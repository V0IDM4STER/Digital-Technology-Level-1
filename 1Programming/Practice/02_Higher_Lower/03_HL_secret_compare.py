# HL Component 3 - Compare secret number to users guess

SECRET = 7

guess = ""

while guess != SECRET:
    
    guess = int(input("Guess: "))

    if guess > SECRET:
        print("Too high. Try a lower number.")
    elif guess < SECRET:
        print("Too low. Try a higher number.")
    else:
        print("Well done! You guessed the secret number.")