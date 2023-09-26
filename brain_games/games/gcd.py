import random


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = 1
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            correct_answer = str(i)
    return f'{str(num1)} {str(num2)}', correct_answer
