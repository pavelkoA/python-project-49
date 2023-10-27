from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import run_game_engine
from brain_games.constant import PROGRES_LENGTH, DESC_PROGRESSION


def get_progression_list(start_num, step):
    return [start_num + step * (number - 1)
            for number in range(PROGRES_LENGTH)]


def get_progression_string(progression_list, correct_answer):
    index_number_answer = progression_list.index(correct_answer)
    progression_list[index_number_answer] = '..'
    return " ".join(map(str, progression_list))


def get_progression_str_and_answer():
    start_num_progression = get_rnd_num()
    step_progression = get_rnd_num(end_num=10)
    progression_list = get_progression_list(start_num_progression,
                                            step_progression)
    correct_answer = get_rnd_choice(progression_list)
    progression_string = get_progression_string(progression_list,
                                                correct_answer)
    return progression_string, correct_answer


def start_game_progression():
    run_game_engine(DESC_PROGRESSION, get_progression_str_and_answer)
