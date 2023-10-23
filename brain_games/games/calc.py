from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import lauche_game_engine
from brain_games.constant import DESC_CALC, MATH_OPERATIONS


def get_math_calculations(num1, num2):
    math_sign = get_rnd_choice(MATH_OPERATIONS)
    match math_sign:
        case '+':
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2
    oper_string = f'{num1} {math_sign} {num2}'
    return oper_string, str(correct_answer)


def get_math_expession_and_answer():
    num1, num2 = get_rnd_num(amount=2)
    oper_string, correct_answer = get_math_calculations(num1, num2)
    return oper_string, correct_answer


def start_game_calc():
    lauche_game_engine(DESC_CALC, get_math_expession_and_answer)
