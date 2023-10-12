from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import play_game
from brain_games.constant import DESC_EVEN


def get_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    number = get_rnd_num()
    correct_answer = get_even(number)
    return str(number), correct_answer


def play_even():
    play_game(DESC_EVEN, even_game)
