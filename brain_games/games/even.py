from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import start_engine_games
from brain_games.constant import DESC_EVEN


def is_even(number):
    return number % 2 == 0


def get_task_game_even():
    number = get_rnd_num()
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer


def start_game_even():
    start_engine_games(DESC_EVEN, get_task_game_even)
