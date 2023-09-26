import random


def even():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
