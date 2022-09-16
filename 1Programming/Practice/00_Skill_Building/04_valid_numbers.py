# Ask user for number
# Loop until valid number is entered
# Make code recyclable

valid = False
while not valid:
    error = "Whoops! Please enter a number between 1 and 10."

    try:
        response = int(input("Enter a number between 1 and 10: "))

        if 1 <= response <= 10:
            valid = True
        else:
            print(error)
            print()
    
    except ValueError:
        print(error)

print(response)
    
