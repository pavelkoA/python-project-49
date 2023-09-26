import random
from brain_games.games.game_logic import question, answer, end_string


def prime(name):
    points = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while points < 3:
        num = random.randint(2, 100)
        correct_answer = 'yes'
        for i in range(2, num):
            if num % i == 0:
                correct_answer = 'no'
                break
        your_answer = question(f'{str(num)}')
        points += answer(your_answer, correct_answer)
    end_string(points, name)
