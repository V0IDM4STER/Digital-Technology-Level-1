# Quiz Quest Full Game
# Version 1.0
# Game Info: 

import random

def question_generator(question, list1, list2):
    global pattern
    global correct_answer
    global incorrect_answers
    global d

    print(list1[question])

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

    pattern1 = [a, b, c, d]
    pattern2 = [d, c, b, a]
    pattern3 = [b, a, d, c]
    pattern4 = [c, d, a, b]
    pattern5 = [d, a, b, c]

    pattern_num = random.randint(1, 5)
    
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
    
    print("A. {}".format(pattern[0]))
    print("B. {}".format(pattern[1]))
    print("C. {}".format(pattern[2]))
    print("D. {}".format(pattern[3]))

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
questions = ["How tall is Mount Cook?", "When did Captain Cook come to New Zealand?", "When did New Zealand gain independence from Britain?",
"What animal can you find on the NZ 1 dollar coin?", "In 1893, New Zealand became the first country to do what?", "What is a Tuatara?",
"When was NZ Rugby Football Union founded?", "When was New Zealand's first Poppy Day?"]
answers = ["3,518 metres", "4,289 metres", "3,945 metres", "3,754 metres", "1709", "1739", "1799", "1769", "1917", "1927", "1937", "1947",
"Kakapo", "Seal", "Takahe", "Kiwi", "Abolish slavery", "Legalise same-sex marriage", "Give workers paid holidays", "Give women the right to vote",
"Mammal", "Bird", "Insect", "Reptile", "1852", "1872", "1902", "1892", "1932", "1943", "1953", "1922"]

num_of_questions = intcheck("How many questions do you want to answer? ", 1, 8)

keep_going = ""

while keep_going == "":

    q_answered = 0
    num_correct = 0
    num_incorrect = 0
    
    while q_answered < num_of_questions:
        
        question = random.randint(0, 7)

        question_generator(question, questions, answers)

        answer = input("Answer: ")
        answer = answer.lower()

        if answer == correct_answer:
            print("Correct!")
            num_correct += 1
        elif answer in incorrect_answers:
            print("Incorrect! The correct answer is {}.".format(d))
            num_incorrect += 1
        else:
            print("Please enter either a, b, c, or d.")
            continue

        q_answered += 1

    print("Correct: {}  |  Incorrect: {}".format(num_correct, num_incorrect))

    keep_going = input("Press <enter> to play again or a letter and <enter> to quit: ")