from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import start_engine_games
from brain_games.constant import DESC_CALC, MATH_OPERATIONS


def get_math_calculations(num1, num2, math_sign):
    match math_sign:
        case '+':
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2
    return str(correct_answer)


def get_string_expression(num1, num2, math_sign):
    return f'{num1} {math_sign} {num2}'


def get_task_game_calc():
    num1, num2 = get_rnd_num(amount=2)
    math_sign = get_rnd_choice(MATH_OPERATIONS)
    correct_answer = get_math_calculations(num1, num2, math_sign)
    oper_string = get_string_expression(num1, num2, math_sign)
    return oper_string, correct_answer


def start_game_calc():
    start_engine_games(DESC_CALC, get_task_game_calc)
