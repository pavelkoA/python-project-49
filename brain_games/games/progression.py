from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import PROGRES_LENGTH, DESCRIPTION_PROGRESSION


def generate_progression_list(start_number, step, progres_length):
    return [start_number + step * (number)
            for number in range(progres_length)]


def get_progression_str_and_missed_num():
    start_number_progression = get_random_number()
    step_progression = get_random_number(end_num=10)
    progression_list = generate_progression_list(start_number_progression,
                                                 step_progression,
                                                 PROGRES_LENGTH)
    hidden_index = get_random_number(start_num=0,
                                     end_num=PROGRES_LENGTH - 1)
    missed_num = progression_list[hidden_index]
    progression_list[hidden_index] = '..'
    return " ".join(map(str, progression_list)), str(missed_num)


def run_game_progression():
    run_game(DESCRIPTION_PROGRESSION, get_progression_str_and_missed_num)
