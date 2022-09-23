import random

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

for item in range (0, 10):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    num1 = int(num1)
    num2 = int(num2)

    user = int(intcheck("What is {} + {}? ".format(num1, num2)))

    answer = int(num1 + num2)

    if user == answer:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is {}.".format(answer))