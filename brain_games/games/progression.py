
from brain_games.rnd_utils import get_rnd_num, get_rnd_choice


def generate_progres_list():
    start_num = get_rnd_num()
    step = get_rnd_num(end_num=10)
    progres_length = 10
    progres_list = []
    while len(progres_list) != progres_length:
        progres_list.append(str(start_num))
        start_num += step
    return progres_list


def play_progression():
    progres_list = generate_progres_list()
    correct_answer = get_rnd_choice(progres_list)
    progres_list[progres_list.index(correct_answer)] = '..'
    return " ".join(progres_list), correct_answer
