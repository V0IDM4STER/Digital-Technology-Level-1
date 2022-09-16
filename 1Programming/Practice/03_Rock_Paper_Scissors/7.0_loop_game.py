# RPS Component 6
# Loop Game

import random

# Answer Checker Function
def answer_check(question):

    # Sets up global variables
    global answer
    global error # Added in component 5

    # Asks the user the desired question
    answer = input(question)
    
    # Makes the variable is_num true
    is_num = True

    # Sets up the error message
    if is_num:
        error = "Please do not enter a number."
    else: 
        error = "Please enter a valid answer."
    
    # Checks if the answer is a number
    try:
        int(answer)
    # If it's not, then is_num is false
    except ValueError:
        is_num = False
        # Returns the answer to the main routine
        return answer
    
    # While the answer is a number
    while is_num:  
        # Gives the user an error message
        print()
        print(error)
        print()
        # Asks the desired question
        answer = input(question)
        
        try:
            # Checks if the answer is a number
            int(answer)
        except ValueError:
            # If it's not, then is_num is false
            is_num = False
            # Returns the answer to the main routine
            return answer

# Number Checker Function
def number_check(question, low = None, high = None):

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

# Main Routine
keep_going = ""
while keep_going == "":
    rounds = number_check("Rounds: ", 1)
    rounds_played = 0
    computer_action = ["Rock", "Paper", "Scissors"] # Need better variable name

    while rounds_played < rounds:

        # Sets up the choices for the computer
        player = answer_check("Please type rock (r), paper (p), or scissors (s): ")

        # Randomly chooses either r, p, or s for the computer
        computer = random.choice(computer_action)

        # Sees what the player chose and decides who won/lost/tied
        if player == "rock" or player == "r":
            print("Computer Chose: {}   |   You Chose: Rock".format(computer))
            if computer == "Rock":
                print("Tie")
            elif computer == "Paper":
                print("You Lose")
            else: 
                print("You Win")

        elif player == "paper" or player == "p":
            print("Computer Chose: {}   |   You Chose: Paper".format(computer))
            if computer == "Rock":
                print("You Win")
            elif computer == "Paper":
                print("Tie")
            else:
                print("You Lose")

        elif player == "scissors" or player == "s":
            print("Computer Chose: {}   |   You Chose: Scissors".format(computer))
            if computer == "Rock":
                print("You Lose")
            elif computer == "Paper":
                print("You Win")
            else:
                print("Tie")
        
        else:
            print()
            print(error)
            print()
            continue

        rounds_played += 1

    print()
    keep_going = input("Press <enter> to play again or a letter to quit: ")
    print()

print("Thank you for playing.")