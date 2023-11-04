from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.constant import DESC_EVEN


def is_even(number):
    return number % 2 == 0


def get_problem_num_and_answer():
    problem_number = get_random_number()
    correct_answer = 'yes' if is_even(problem_number) else 'no'
    return problem_number, str(correct_answer)


def start_game_even():
    run_game(DESC_EVEN, get_problem_num_and_answer)
