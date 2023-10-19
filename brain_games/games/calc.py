from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import launch_games
from brain_games.constant import DESC_CALC, MATH_OPERATIONS


def math_calculations(num1, num2, math_sign):
    match math_sign:
        case '+':
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2
    return (f'{num1} {math_sign} {num2}',
            str(correct_answer))


def get_task_game_calc():
    num1, num2 = get_rnd_num(amount=2)
    math_sign = get_rnd_choice(MATH_OPERATIONS)
    oper_string, correct_answer = math_calculations(num1, num2,
                                                    math_sign)
    return oper_string, correct_answer


def start_game_calc():
    launch_games(DESC_CALC, get_task_game_calc)
