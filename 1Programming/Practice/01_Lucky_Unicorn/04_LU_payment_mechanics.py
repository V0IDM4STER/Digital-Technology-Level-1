# Lucky Unicorn Decomposition Step 4 - Payment Mechanics

# To do
# Assume starting amount is $10
# Allow manual token input for testing purposes
# Adjust total correctly for a given token
#    - If it's a unicorn, add $5
#    - If it's a zebra or horse, subtract $0.5
#    - If it's a donkey, subtract $1
# Give user feedback based on winnings
# State new total

# Assume starting amount is $10
total = 10

# Allow manual token input for testing purposes
token = input("Enter a token: ")

# Adjust total correctly for given token
if token == "unicorn":
    total += 5
    feedback = "Congratulations! You got a lucky unicorn and have won $5.00."
elif token == "donkey":
    total -= 1
    feedback = "Sorry, you didn't win anything this round."
else:
    total -= 0.5
    feedback = "Congratulations! You won 50c."

print()

print(feedback)
print("You have ${:.2f} to play with.".format(total))