from brain_games.rnd_utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESC_PRIME


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_required_number_and_answer():
    number = get_random_number(start_num=2)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, str(correct_answer)


def start_game_prime():
    run_game(DESC_PRIME, get_required_number_and_answer)
