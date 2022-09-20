import random

def function1(question, list1, list2):
    global pattern
    global correct_answer

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
    elif pattern_num == 2:
        pattern = pattern2
        correct_answer = "a"
    elif pattern_num == 3:
        pattern = pattern3
        correct_answer = "c"
    elif pattern_num == 4:
        pattern = pattern4
        correct_answer = "b"
    else:
        pattern = pattern5
        correct_answer = "a"
    
    print(*pattern, sep='\n')

questions = ["Q1", "Q2", "Q3"]
answers = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12"]

question = random.randint(0, 2)

function1(question, questions, answers)

answer = input("Answer: ")
answer = answer.lower()

if answer == correct_answer:
    print("Correct!")
else:
    print("Incorrect!")