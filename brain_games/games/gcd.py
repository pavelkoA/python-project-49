from math import gcd
from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import lauche_game_engine
from brain_games.constant import DESC_GCD


def get_gcd(num1, num2):
    return str(gcd(num1, num2))


def get_gcd_and_answer():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = get_gcd(num1, num2)
    return f'{num1} {num2}', correct_answer


def start_game_gcd():
    lauche_game_engine(DESC_GCD, get_gcd_and_answer)
