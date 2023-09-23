import random
from brain_games.cli import answer, question


def calc(name):
    points = 0
    print('What is the result of the expression?')
    while points < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operac = random.choice(['+', '-', '*'])
        correct_answer = 0
        match operac:
            case '+':
                correct_answer = str(num1 + num2)
            case "-":
                correct_answer = str(num1 - num2)
            case "*":
                correct_answer = str(num1 * num2)
        your_answer = question(f'{str(num1)} {operac} {str(num2)}')
        points += answer(your_answer, correct_answer)
    print(f"Congratulations, {name}!" if points == 3 else f"Let's try again, {name}")
