from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import play_game
from math import gcd


DESC_GCD = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = str(gcd(num1, num2))
    return f'{str(num1)} {str(num2)}', correct_answer


def play_gcd():
    play_game(DESC_GCD, gcd_game)
