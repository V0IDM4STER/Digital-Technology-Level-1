# HL Component 7 - Generates desired number of rounds

rounds = int(input("How many rounds do you want to play? "))
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played + 1))
    rounds_played += 1

print("You have reached the end of the game.")