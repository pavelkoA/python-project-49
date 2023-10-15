from math import gcd
from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import launch_games
from brain_games.constant import DESC_GCD


def gcd_game():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = str(gcd(num1, num2))
    return f'{str(num1)} {str(num2)}', correct_answer


def start_game_gcd():
    launch_games(DESC_GCD, gcd_game)
