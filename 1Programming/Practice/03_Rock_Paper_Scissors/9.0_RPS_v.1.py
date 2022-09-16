# RPS Full Game
# Version 1.0

import random

# Answer Checker Function
def answer_check(question):

    # Sets up global variables
    global answer
    error = "Please don't enter a number."

    # Asks the user the desired question
    answer = input(question)
    
    # Makes the variable is_num true
    is_num = True 
    
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
        print("### Round {} of {} ###".format(rounds_played + 1, rounds))
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

# Statement Generator Function
def rps_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Main Routine
keep_going = ""
while keep_going == "":
    
    global rounds_played
    global rounds
    rounds = number_check("Rounds: ", 1)
    print()
    rounds_played = 0
    computer_action = ["Rock", "Paper", "Scissors"] # Need better variable name
    num_won = 0
    num_draw = 0
    num_lost = 0

    while rounds_played < rounds:

        print("Round {} of {}".format(rounds_played + 1, rounds))

        # Gets user choice
        player = answer_check("Please type rock (r), paper (p), or scissors (s): ")
        player = (player.lower())

        # Randomly chooses either r, p, or s for the computer
        computer = random.choice(computer_action)

        # Sees what the player chose and decides who won/lost/tied
        if player == "rock" or player == "r":
            if computer == "Rock":
                num_draw += 1
                rps_statement("Computer Chose: {}   |   You Chose: Rock  |  Result: It's a tie".format(computer), "-")
            elif computer == "Paper":
                num_lost += 1
                rps_statement("Computer Chose: {}   |   You Chose: Rock  |  Result: You lost".format(computer), "#")
            else: 
                num_won += 1
                rps_statement("Computer Chose: {}   |   You Chose: Rock  |  Result: You win!".format(computer), "*")      

        elif player == "paper" or player == "p":
            print()
            print("Computer Chose: {}   |   You Chose: Paper".format(computer))
            if computer == "Rock":
                print("You Win")
                num_won += 1
            elif computer == "Paper":
                print("Tie")
                num_draw += 1
            else:
                print("You Lose")
                num_lost += 1

        elif player == "scissors" or player == "s":
            print()
            print("Computer Chose: {}   |   You Chose: Scissors".format(computer))
            if computer == "Rock":
                print("You Lose")
                num_lost += 1
            elif computer == "Paper":
                print("You Win")
                num_won += 1
            else:
                print("Tie")
                num_draw += 1
        
        else:
            print()
            print("Please enter a valid answer.")
            continue

        rounds_played += 1

    print()
    print("******** End Game Summary ********")
    print("Won: {}  |  Lost: {}  |  Draw: {}".format(num_won, num_lost, num_draw))
    print("**********************************")

    print()
    keep_going = input("Press <enter> to play again or a letter to quit: ")
    print()

print("Thanks for playing.")