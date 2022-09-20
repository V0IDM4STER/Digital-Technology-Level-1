import random

def function1(question):
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
    
    print(a)
    print(b)
    print(c)
    print(d)

list1 = ["Q1", "Q2", "Q3"]
list2 = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12"]

question = random.randint(0, 2)

function1(question)