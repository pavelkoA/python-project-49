import math
from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESCRIPTION_GCD


def get_gcd(number_first, number_second):
    return math.gcd(number_first, number_second)


def get_numbers_and_gcd():
    number_first, number_second = get_random_number(), get_random_number()
    correct_answer = get_gcd(number_first, number_second)
    numbers_string = f'{number_first} {number_second}'
    return numbers_string, str(correct_answer)


def run_game_gcd():
    run_game(DESCRIPTION_GCD, get_numbers_and_gcd)
