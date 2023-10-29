from brain_games.rnd_utils import get_random_number, get_rnd_choice
from brain_games.engine import run_game
from brain_games.constant import DESC_CALC, MATH_OPERATIONS


def get_math_calculations(number_first, number_second, math_sign):
    match math_sign:
        case '+':
            return number_first + number_second
        case "-":
            return number_first - number_second
        case "*":
            return number_first * number_second


def get_math_expession_and_answer():
    number_first, number_second = get_random_number(), get_random_number()
    math_sign = get_rnd_choice(MATH_OPERATIONS)
    correct_answer = get_math_calculations(number_first,
                                           number_second,
                                           math_sign)
    oper_string = f'{number_first} {math_sign} {number_second}'
    return oper_string, str(correct_answer)


def start_game_calc():
    run_game(DESC_CALC, get_math_expession_and_answer)
