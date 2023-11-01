from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESC_EVEN


def is_even(number):
    return number % 2 == 0


def get_required_num_and_answer():
    number = get_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, str(correct_answer)


def start_game_even():
    run_game(DESC_EVEN, get_required_num_and_answer)
