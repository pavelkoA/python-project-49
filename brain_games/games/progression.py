import random


def progression():
    start_num = random.randint(1, 100)
    step = random.randint(1, 10)
    progres_list = []
    while len(progres_list) != 10:
        progres_list.append(str(start_num))
        start_num += step
    correct_answer = random.choice(progres_list)
    progres_list[progres_list.index(correct_answer)] = '..'
    return " ".join(progres_list), correct_answer
