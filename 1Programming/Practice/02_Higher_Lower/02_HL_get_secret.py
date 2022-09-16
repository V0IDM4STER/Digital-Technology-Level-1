# HL Component 2 - Generates random number between low and high


import random

LOW = 1
HIGH = 4

# Choose 20 numbers between LOW and HIGH and then print them
for item in range(0,20):
    secret = random.randint(LOW, HIGH)
    print(secret, end="\t") # end \t puts items on new line