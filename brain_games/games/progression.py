from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import PROGRES_LENGTH, DESCRIPTION_PROGRESSION


def get_progression_list(start_number, step):
    return [start_number + step * (number - 1)
            for number in range(PROGRES_LENGTH)]


def get_progression_with_missing_number(progression_list,
                                        response_index):
    progression_list[response_index] = '..'
    return progression_list


def get_progression_str_and_missed_num():
    start_number_progression = get_random_number()
    step_progression = get_random_number(end_num=10)
    progression_list = get_progression_list(start_number_progression,
                                            step_progression)
    response_index = get_random_number(end_num=PROGRES_LENGTH - 1)
    correct_answer = progression_list[response_index]
    progression_string = get_progression_with_missing_number(progression_list,
                                                             response_index)
    return " ".join(map(str, progression_string)), str(correct_answer)


def run_game_progression():
    run_game(DESCRIPTION_PROGRESSION, get_progression_str_and_missed_num)
