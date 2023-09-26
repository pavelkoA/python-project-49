import prompt


def answer(your, correct):
    if correct == your:
        print('Correct!')
        return 1
    else:
        print(f"Your answer: '{your}' is wrong answer ;(."
              f"Correct answer was '{correct}'")
        return 5


def question(quest):
    print(f"Question: {quest}")
    return prompt.string("Your answer: ")


def end_string(points, name):
    if points == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
