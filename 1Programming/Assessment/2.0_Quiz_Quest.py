# Quiz Quest Full Game
# Version 2.0 (With Colour)
# Author: Daniel Hesp
# Date Created: 30/09/2022
# Game Info: This is a game coded in Python. It is a multiple-choice quiz game featuring New Zealand trivia questions.

# !!! IMPORTANT !!!
# This version of the game features coloured messages. If you do not have the termcolor module installed, this game will not work.
# To install the termcolor module on Windows or macOS, simply open the terminal and type: pip install termcolor.
# If this does not work, you can swap to the colourless version.

# Import Required Modules
import random
from termcolor import colored

# Question + Answer Generator Function
def question_generator(question, list1, list2):
    # Set up global variables
    global pattern
    global correct_answer
    global incorrect_answers
    global d

    # Print the question
    print(list1[question])

    # Get answers from answer list
    if question == 0:
        a = list2[0]
        b = list2[1]
        c = list2[2]
        d = list2[3]
    
    else:
        question += 1

        a_raw = question * 4 - 4
        a = list2[a_raw]
        b_raw = question * 4 - 3
        b = list2[b_raw]
        c_raw = question * 4 - 2
        c = list2[c_raw]
        d_raw = question * 4 - 1
        d = list2[d_raw]

    # Set up answer patterns and choose one
    pattern1 = [a, b, c, d]
    pattern2 = [d, c, b, a]
    pattern3 = [b, a, d, c]
    pattern4 = [c, d, a, b]
    pattern5 = [d, a, b, c]

    pattern_num = random.randint(1, 5)
    
    # Set correct/incorrect answers depending on pattern
    if pattern_num == 1:
        pattern = pattern1
        correct_answer = "d"
        incorrect_answers = ["a", "b", "c"]
    elif pattern_num == 2:
        pattern = pattern2
        correct_answer = "a"
        incorrect_answers = ["b", "c", "d"]
    elif pattern_num == 3:
        pattern = pattern3
        correct_answer = "c"
        incorrect_answers = ["a", "b", "d"]
    elif pattern_num == 4:
        pattern = pattern4
        correct_answer = "b"
        incorrect_answers = ["a", "c", "d"]
    else:
        pattern = pattern5
        correct_answer = "a"
        incorrect_answers = ["b", "c", "d"]
    
    # Print possible answers
    print("A. {}".format(pattern[0]))
    print("B. {}".format(pattern[1]))
    print("C. {}".format(pattern[2]))
    print("D. {}".format(pattern[3]))

# Input Checking Function
def intcheck(question, low = None, high = None):

    # Sets up error message
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {}. ".format(low, high)
    
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
                print()
                print(colored("{}".format(error), 'red'))
                print()
                continue
            
            # Checks that response is not too high
            if high is not None and response > high:
                print()
                print(colored("{}".format(error), 'red'))
                print()
                continue

            return response
        
        except ValueError:
            print() 
            print(colored("{}".format(error), 'red'))
            print()
            continue

# Main Routine
# List of Possible Questions 
questions = ["How tall is Mount Cook?", "When did Captain Cook come to New Zealand?", "When did New Zealand gain independence from Britain?",
"What animal can you find on the NZ 1 dollar coin?", "In 1893, New Zealand became the first country to do what?", "What is a Tuatara?",
"When was NZ Rugby Football Union founded?", "When was New Zealand's first Poppy Day?", "New Zealand's highest mountain has been known by two names over the years. One is Mount Cook. What is the other?", 
"Approximately what percentage of of the population of New Zealand is Maori?", "What was the kiwi-fruit first known as?", "'Kai Moana' is the base of the Maori diet. What does it mean?", 
"How much of the land in New Zealand is used for agriculture?", "When did hamburger and pizza fast-food reach New Zealand?", 
"The name 'New Zealand' in Maori is Aotearoa. What does this translate to in English?", "How many peaks does the South Island of New Zealand have?", 
"What is the main religion of New Zealand?", "What is the closest country to New Zealand?", "What is the biggest city in New Zealand?", 
"What is the longest river in New Zealand?"]

# Corresponding List of Answers For Questions
answers = ["3,518 metres", "4,289 metres", "3,945 metres", "3,754 metres", "1709", "1739", "1799", "1769", "1917", "1927", "1937", "1947",
"Kakapo", "Seal", "Takahe", "Kiwi", "Abolish slavery", "Legalise same-sex marriage", "Give workers paid holidays", "Give women the right to vote", 
"Mammal", "Bird", "Insect", "Reptile", "1852", "1872", "1902", "1892", "1932", "1943", "1953", "1922", "Allenby", "Adam Joachim", "Arethusa", "Aoraki", 
"90%", "65%", "30%", "10%", "The Japanese Apple", "The Thai Starfruit", "The Indian Greengage", "The Chinese Gooseberry", "Food From The Ground", 
"Food From The Animals", "Food From The Trees", "Food From The Sea", "3%", "60%", "42%", "15%", "1950s", "1980s", "1970s", "1960s", 
"Land of Peace and Water", "Land of the Pink Flowers", "Land of The Two Green Islands", "Land of The Long White Cloud", "27", "6", "10", "18", 
"Buddhism", "Islam", "The Ratana Church", "Christianity", "Chile", "Antigua and Barbuda", "Spain", "Australia", "Hamilton", "Christchurch", 
"Wellington", "Auckland", "Taieri River", "Whanganui River", "Clutha River", "Waikato River"]

# Introduction
print()
print("*** Welcome to the NZ Trivia Quiz Game ***")
print()
print("In this game, you'll answer a series of questions based around New Zealand history, geography, and culture.")

# Set up and begin game loop
keep_going = ""

while keep_going == "":

    # Ask the user how many questions they want to answer
    print()
    num_of_questions = intcheck("How many questions do you want to answer? ", 1,20)
    print()
    
    # Set game score variables
    q_answered = 0
    num_correct = 0
    num_incorrect = 0

    # Set up list of already asked questions
    already_asked_small = []
    already_asked_large = []

    valid_answer = False
    
    # Begin question loop
    while q_answered < num_of_questions:
        
        # Choose random question number
        question = random.randint(0, 19)

        # Prevent duplicate questions
        if question <= 9:
            if question in already_asked_small:
                continue
        elif question > 9:
            if question in already_asked_large:
                continue

        while valid_answer == False:
            
            # Generate question + answers, print 
            question_generator(question, questions, answers)

            # Get user's answer
            answer = input("Answer: ")
            answer = answer.lower()

            # Decide if the answer is correct, print appopriate feedback, add 1 to appropriate score 
            if answer == correct_answer:
                print()
                print(colored("Correct!", 'green'))
                print()
                num_correct += 1
                valid_answer = True
            elif answer in incorrect_answers:
                print()
                print(colored("Incorrect! ", "red") + "The correct answer is {}.".format(d))
                print()
                num_incorrect += 1
                valid_answer = True
            else:
                print()
                print(colored("Please enter either A, B, C, or D.", 'red'))
                print()

        # Add question number to list for already asked questions
        if question <= 9:
            already_asked_small.append(question)
        elif question > 9:
            already_asked_large.append(question)
        
        # Add 1 to number of questions answered
        q_answered += 1

        valid_answer = False

    # Print game scores
    print("-------------  Game Scores  -------------")
    print(" ---  Correct: {}  |  Incorrect: {}  ---".format(num_correct, num_incorrect))
    print("-----------------------------------------")

    # Ask user if they want to play again
    print()
    keep_going = input("Press <enter> to play again or a letter and <enter> to quit: ")