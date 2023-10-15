from brain_games.rnd_utils import get_rnd_math_expression
from brain_games.engine import launch_games
from brain_games.constant import DESC_CALC


def calc_game():
    oper_string = get_rnd_math_expression()
    correct_answer = str(eval(oper_string))
    return oper_string, correct_answer


def start_game_calc():
    launch_games(DESC_CALC, calc_game)
