# Ask user for number
# Loop until valid number is entered
# Make code recyclable

# function goes here
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

# ask user for name
name = input("What is your name? ")

#ask user for two numbers
num_1 = intcheck("Enter a number between 1 and 15: ", 1, 15)
num_2 = intcheck("Enter a number between 5 and 10: ", 5, 10)

# add numbers together
add = num_1 + num_2

# greet user and display math
print("Hello", name)

print("{} + {} = {}".format(num_1, num_2, add))