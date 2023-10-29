from math import gcd
from brain_games.rnd_utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESC_GCD


def get_gcd(number_first, number_second):
    return gcd(number_first, number_second)


def get_numbers_and_gcd():
    number_first, number_second = get_random_number(), get_random_number()
    correct_answer = get_gcd(number_first, number_second)
    numbers_string = f'{number_first} {number_second}'
    return numbers_string, str(correct_answer)


def start_game_gcd():
    run_game(DESC_GCD, get_numbers_and_gcd)
