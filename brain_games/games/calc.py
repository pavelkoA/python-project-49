import random
import prompt


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
                correct_answer = num1 + num2
            case "-":
                correct_answer = num1 - num2
            case "*":
                correct_answer = num1 * num2
        print(f'Question: {str(num1)} {operac} {str(num2)}')
        your_answer = prompt.integer('Your answer: ')

        if correct_answer == your_answer:
            print('Correct!')
            points += 1
        else:
            break
    if points == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{your_answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!'")
         
