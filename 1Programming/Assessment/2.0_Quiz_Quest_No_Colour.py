# Quiz Quest Full Game
# Version 2.0 (Without Colour)
# Author: Daniel Hesp
# Date Created: 30/09/2022
# Game Info: This is a game coded in Python. It is a multiple-choice quiz game featuring New Zealand trivia questions.

# Import Required Modules
import random

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
                print()
                print(error)
                print()
                continue
            
            # Checks that response is not too high
            if high is not None and response > high:
                print()
                print(error)
                print()
                continue

            return response
        
        except ValueError:
            print() 
            print(error)
            print()
            continue

# Main Routine
# List of Possible Questions 
questions = ["How tall is Mount Cook?", "When did Captain Cook come to New Zealand?", "When did New Zealand gain independence from Britain?",
"What animal can you find on the NZ 1 dollar coin?", "In 1893, New Zealand became the first country to do what?", "What is a Tuatara?",
"When was NZ Rugby Football Union founded?", "When was New Zealand's first Poppy Day?"]

# Corresponding List of Answers For Questions
answers = ["3,518 metres", "4,289 metres", "3,945 metres", "3,754 metres", "1709", "1739", "1799", "1769", "1917", "1927", "1937", "1947",
"Kakapo", "Seal", "Takahe", "Kiwi", "Abolish slavery", "Legalise same-sex marriage", "Give workers paid holidays", 
"Give women the right to vote", "Mammal", "Bird", "Insect", "Reptile", "1852", "1872", "1902", "1892", "1932", "1943", "1953", "1922"]

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
    num_of_questions = intcheck("How many questions do you want to answer? ", 1, 8)
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
        question = random.randint(0, 7)

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
                print("Correct!")
                print()
                num_correct += 1
                valid_answer = True
            elif answer in incorrect_answers:
                print()
                print("Incorrect! The correct answer is {}.".format(d))
                print()
                num_incorrect += 1
                valid_answer = True
            else:
                print()
                print("Please enter either A, B, C, or D.")
                print()

        # Add question number to list for already asked questions
        if question <= 9:
            already_asked_small.append(question)
        elif question > 9:
            already_asked_large(question)
        
        # Add 1 to number of questions answered
        q_answered += 1

        valid_answer = False

    # Print game scores
    print("------------  Game Scores  ------------")
    print("---  Correct: {}  |  Incorrect: {}  ---".format(num_correct, num_incorrect))
    print("---------------------------------------")

    # Ask user if they want to play again
    print()
    keep_going = input("Press <enter> to play again or a letter and <enter> to quit: ")