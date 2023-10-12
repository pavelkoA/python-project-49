
from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import play_game
from brain_games.constant import PROGRES_LENGTH


DESC_PROGRESSION = 'What number is missing in the progression?'


def generate_progres_list():
    start_num = get_rnd_num()
    step = get_rnd_num(end_num=10)
    progres_list = []
    while len(progres_list) != PROGRES_LENGTH:
        progres_list.append(str(start_num))
        start_num += step
    return progres_list


def progression_game():
    progres_list = generate_progres_list()
    correct_answer = get_rnd_choice(progres_list)
    progres_list[progres_list.index(correct_answer)] = '..'
    return " ".join(progres_list), correct_answer


def play_progression():
    play_game(DESC_PROGRESSION, progression_game)
