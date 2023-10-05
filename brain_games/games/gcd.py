from brain_games.rnd_utils import get_rnd_num
from math import gcd


def play_gcd():
    num1, num2 = get_rnd_num(amount=2)
    correct_answer = gcd(num1, num2)
    return f'{str(num1)} {str(num2)}', correct_answer
