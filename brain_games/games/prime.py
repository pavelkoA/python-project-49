import random


def prime():
    num = random.randint(2, 100)
    correct_answer = 'yes'
    for i in range(2, num):
        if num % i == 0:
            correct_answer = 'no'
            break
    return str(num), correct_answer
