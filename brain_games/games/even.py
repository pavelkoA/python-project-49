import prompt
import random

def answer(your_answer, correct_answer):
    if correct_answer == your_answer:
            print('Correct!')
    else:
        print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        return break

def even(name):
    points = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        your_answer = prompt.string("Your answer: ")
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        answer(your_answer, correct_answer)
        # if correct_answer == your_answer:
        #     print('Correct!')
        # else:
        #     print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        #     break
    print(f"Congratulations, {name}!" if points == 3 else f"Let's try again, {name}")

