import random


def calc():
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
    return f'{str(num1)} {operac} {str(num2)}', correct_answer
