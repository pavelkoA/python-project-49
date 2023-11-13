from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESCRIPTION_EVEN


def is_even(number):
    return number % 2 == 0


def get_problem_num_and_answer():
    problem_number = get_random_number()
    correct_answer = 'yes' if is_even(problem_number) else 'no'
    return problem_number, correct_answer


def run_game_even():
    run_game(DESCRIPTION_EVEN, get_problem_num_and_answer)
