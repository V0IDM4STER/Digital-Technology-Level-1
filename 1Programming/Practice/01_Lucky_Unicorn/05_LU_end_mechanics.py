# Lucky Unicorn Decomposition Step 5 - End Mechanics

# To do
# Ask user how much money they want to play with. 
# If the total is less than $1, quit.
# If the total is more than $1, ask the user if the want to keep going.


# Ask user how much money they want to play with.
total = int(input("How much would you like to play with? "))

keep_going = ""
while keep_going == "":

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

    if total < 1:
        print("Sorry, you don't have enough money to continue.")
        print()
        print("Game Over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to continue playing or any other key to quit.")

print()
print("Thank you for playing.")
print()