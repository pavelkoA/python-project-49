from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import launch_games
from brain_games.constant import DESC_CALC, MATH_OPER


def get_rnd_math_expression() -> str:
    num1, num2 = get_rnd_num(amount=2)
    math_sign = get_rnd_choice(MATH_OPER)
    return f'{str(num1)} {math_sign} {str(num2)}'


def get_task_game_calc():
    oper_string = get_rnd_math_expression()
    correct_answer = str(eval(oper_string))
    return oper_string, correct_answer


def start_game_calc():
    launch_games(DESC_CALC, get_task_game_calc)
