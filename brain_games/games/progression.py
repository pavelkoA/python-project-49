
from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import start_engine_games
from brain_games.constant import PROGRES_LENGTH, DESC_PROGRESSION


def get_progression_list():
    start_num = get_rnd_num()
    step = get_rnd_num(end_num=10)
    progres_list = [str(start_num + step * (number - 1))
                    for number in range(PROGRES_LENGTH)]
    return progres_list


def get_task_game_progression():
    progression_list = get_progression_list()
    rnd_index = get_rnd_num(end_num=PROGRES_LENGTH - 1)
    correct_answer = progression_list[rnd_index]
    progression_list[rnd_index] = '..'
    return " ".join(progression_list), correct_answer


def start_game_progression():
    start_engine_games(DESC_PROGRESSION, get_task_game_progression)
