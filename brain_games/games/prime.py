from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESCRIPTION_PRIME


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_required_number_and_answer():
    problem_number = get_random_number(start_num=2)
    correct_answer = 'yes' if is_prime(problem_number) else 'no'
    return problem_number, correct_answer


def run_game_prime():
    run_game(DESCRIPTION_PRIME, get_required_number_and_answer)
