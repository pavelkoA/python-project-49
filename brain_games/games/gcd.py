from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import play_game
from math import gcd


NAME_GAME_GCD = 'gcd'


def gcd_game():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = gcd(num1, num2)
    return f'{str(num1)} {str(num2)}', correct_answer


def play_gcd():
    play_game(NAME_GAME_GCD, gcd_game)
