from math import gcd
from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import run_game_engine
from brain_games.constant import DESC_GCD


def get_gcd(num1, num2):
    return gcd(num1, num2)


def get_numbers_and_gcd():
    num1, num2 = get_rnd_num(), get_rnd_num()
    correct_answer = get_gcd(num1, num2)
    return f'{num1} {num2}', correct_answer


def start_game_gcd():
    run_game_engine(DESC_GCD, get_numbers_and_gcd)
