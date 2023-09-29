from brain_games.engine import get_rnd_num


def get_max_divider(num1, num2):
    correct_answer = 1
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            correct_answer = str(i)
    return correct_answer


def play_gcd():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = get_max_divider(num1, num2)
    return f'{str(num1)} {str(num2)}', correct_answer
