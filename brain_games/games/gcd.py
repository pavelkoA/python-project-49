import random
from brain_games.cli import question, answer, end_string


def gcd(name):
    points = 0
    print('Find the greatest common divisor of given numbers.')
    while points < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = 1
        for i in range(1, max(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                correct_answer = str(i)
        your_answer = question(f'{str(num1)} {str(num2)}')
        points += answer(your_answer, correct_answer)
    end_string(points, name)
