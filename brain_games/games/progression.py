import random
from brain_games.games.game_logic import answer, question, end_string


def progression(name):
    points = 0
    print('What number is missing in the progression?')
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
