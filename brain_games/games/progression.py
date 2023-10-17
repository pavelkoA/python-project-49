
from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import launch_games
from brain_games.constant import PROGRES_LENGTH, DESC_PROGRESSION


def get_progres_list():
    start_num = get_rnd_num()
    step = get_rnd_num(end_num=10)
    progres_list = []
    while len(progres_list) != PROGRES_LENGTH:
        progres_list.append(str(start_num))
        start_num += step
    return progres_list


def get_task_game_progression():
    progres_list = get_progres_list()
    correct_answer = get_rnd_choice(progres_list)
    progres_list[progres_list.index(correct_answer)] = '..'
    return " ".join(progres_list), correct_answer


def start_game_progression():
    launch_games(DESC_PROGRESSION, get_task_game_progression)
