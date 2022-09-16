# Lucky Unicorn DEcomposition Step 3
# Generate a random token

# To do
# Set up starting amount
# Choose 100 tokens (ie: play 100 rounds and ...
#   count # of unicorn and multiply by 5
#   count # of horse / zebra and multiply by 0.5
#   count # of donkey
#   work out total won / lost

from cgitb import Hook
import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

unicorn_count = 0
horse_zebra_count = 0
donkey_count = 0

for item in range (0,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        horse_zebra_count += 1 

    print(chosen)

# Money Calculations
winnings = unicorn_count * 5 + horse_zebra_count *0.5

print("**** Win / Loss Calculations ***")
print("Number of Unicorns: {}".format(unicorn_count))
print("Number of Zebras + Horses: {}".format(horse_zebra_count))
print("Number of Donkeys: {}".format(donkey_count))

print()
print("You spent ${}".format(HOW_MUCH))
print("You go home with ${}".format(winnings))