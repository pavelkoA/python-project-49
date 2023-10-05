from brain_games.rnd_utils import get_rnd_num, get_rnd_choice
from brain_games.engine import play_game


def calculate(num1, num2, oper):
    correct_answer = 0
    match oper:
        case '+':
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2
    return str(correct_answer)


def calc_game():
    math_oper = ['+', '-', '*']
    num1, num2 = get_rnd_num(amount=2)
    oper = get_rnd_choice(math_oper)
    correct_answer = calculate(num1, num2, oper)
    return f'{str(num1)} {oper} {str(num2)}', correct_answer


def play_calc():
    name_game = 'calc'
    play_game(name_game, calc_game)