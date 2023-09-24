import random
from brain_games.cli import answer, question, end_string


def progression(name):
    points = 0
    print('What is the result of the expression?')
    while points < 3:
        start_num = random.randint(1, 100)
        step = random.randint(1, 10)
        progres_list = []
        while len(progres_list) != 10:
            progres_list.append(str(start_num))
            start_num += step
        correct_answer = random.choice(progres_list)
        progres_list[progres_list.index(correct_answer)] = '..'
        your_answer = question(" ".join(progres_list))
        points += answer(your_answer, correct_answer)
    end_string(points, name)
