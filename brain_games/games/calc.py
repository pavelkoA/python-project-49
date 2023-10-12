from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import play_game
from brain_games.constant import MATH_OPER, DESC_CALC


def calc_game():
    num1, num2 = get_rnd_num(amount=2)
    oper = get_rnd_choice(MATH_OPER)
    oper_string = f'{str(num1)} {oper} {str(num2)}'
    correct_answer = str(eval(oper_string))
    return oper_string, correct_answer


def play_calc():
    play_game(DESC_CALC, calc_game)
