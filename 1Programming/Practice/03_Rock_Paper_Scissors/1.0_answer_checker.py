# RPS Component 1 (Part 1)
# Get user input and check it


def answer_check(question):

    # Sets up answer as a global variable
    global answer

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
        print(error)
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
    
        
# Main Routine
answer_check("Please enter anything that isn't a number: ")
print(answer)