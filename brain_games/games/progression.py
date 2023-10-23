
from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import lauche_game_engine
from brain_games.constant import PROGRES_LENGTH, DESC_PROGRESSION


def get_progression_list():
    start_num = get_rnd_num()
    step = get_rnd_num(end_num=10)
    progres_list = [str(start_num + step * (number - 1))
                    for number in range(PROGRES_LENGTH)]
    return progres_list


def get_progression_str_and_answer():
    progression_list = get_progression_list()
    rnd_index = get_rnd_num(end_num=PROGRES_LENGTH - 1)
    correct_answer = progression_list[rnd_index]
    progression_list[rnd_index] = '..'
    return " ".join(progression_list), correct_answer


def start_game_progression():
    lauche_game_engine(DESC_PROGRESSION, get_progression_str_and_answer)
