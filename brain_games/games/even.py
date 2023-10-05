from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import play_game


def get_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    number = get_rnd_num()
    correct_answer = get_even(number)
    return str(number), correct_answer


def play_even():
    name_game = 'calc'
    play_game(name_game, even_game)