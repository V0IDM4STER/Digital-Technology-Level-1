#Lucky Unicorn Decomposition Step 1
#Get initial amount and check that it's valid

# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter a number between {} and {}.".format(low, high)

        try:
            response = int(input("Enter a number between {} and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)
            print()

# main routine goes here

how_much = intcheck("How much money do you want to play with? ", 1, 10)