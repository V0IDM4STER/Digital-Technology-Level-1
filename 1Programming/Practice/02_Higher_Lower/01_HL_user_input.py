# HL - Get (and Check) user input

# To Do
# Check that lowest is an integer (any integer)
# Check that highest is an integer more than lowest
# Check that rounds is more than 1
# Check that guess is between lowest and highest


# Number checking function

def intcheck(question, low = None, high = None):

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

lowest = intcheck("Lowest Number: ")
highest = intcheck("Highest Number: ", lowest + 1) 
rounds = intcheck("Rounds: ", 1)
guess = intcheck("Guess: ", lowest, highest)