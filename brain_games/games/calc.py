from brain_games.engine import get_rnd_num, get_rnd_choice

def calculate(num1, num2, operac):
    correct_answer = 0
    match operac:
        case '+':
            correct_answer = str(num1 + num2)
        case "-":
            correct_answer = str(num1 - num2)
        case "*":
            correct_answer = str(num1 * num2)
    return correct_answer


def play_calc():
    num1, num2 = get_rnd_num(amount=2)
    operac = get_rnd_choice(['+', '-', '*'])
    correct_answer = calculate(num1, num2, operac)
    return f'{str(num1)} {operac} {str(num2)}', correct_answer
