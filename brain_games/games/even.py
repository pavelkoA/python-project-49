import prompt
import random
from brain_games.cli import answer, question
        

def even(name):
    points = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while points < 3:
        number = random.randint(1, 100)
        your_answer = question(number)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        points += answer(your_answer, correct_answer)
    print(f"Congratulations, {name}!" if points == 3 else f"Let's try again, {name}")
