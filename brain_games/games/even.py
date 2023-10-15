from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import launch_games
from brain_games.constant import DESC_EVEN


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    number = get_rnd_num()
    correct_answer = is_even(number)
    return str(number), correct_answer


def start_game_even():
    launch_games(DESC_EVEN, even_game)
