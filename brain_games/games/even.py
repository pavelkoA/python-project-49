from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import run_game_engine
from brain_games.constant import DESC_EVEN


def is_even(number):
    return number % 2 == 0


def get_even_num_and_answer():
    number = get_rnd_num()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer


def start_game_even():
    run_game_engine(DESC_EVEN, get_even_num_and_answer)
