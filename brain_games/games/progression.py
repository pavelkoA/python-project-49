from brain_games.utils import get_random_number, get_rnd_choice
from brain_games.engine import run_game
from brain_games.constant import PROGRES_LENGTH, DESC_PROGRESSION


def get_progression_list(start_number, step):
    return [start_number + step * (number - 1)
            for number in range(PROGRES_LENGTH)]


def get_progression_with_missing_number(progression_list, correct_answer):
    index_number_answer = progression_list.index(correct_answer)
    progression_list[index_number_answer] = '..'
    return " ".join(map(str, progression_list))


def get_progression_str_and_answer():
    start_number_progression = get_random_number()
    step_progression = get_random_number(end_num=10)
    progression_list = get_progression_list(start_number_progression,
                                            step_progression)
    correct_answer = get_rnd_choice(progression_list)
    progression_string = get_progression_with_missing_number(progression_list,
                                                             correct_answer)
    return progression_string, str(correct_answer)


def start_game_progression():
    run_game(DESC_PROGRESSION, get_progression_str_and_answer)
