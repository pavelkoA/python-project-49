import prompt


def welkome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def answer(your, correct):
    if correct == your:
        print('Correct!')
        return 1
    else:
        print(f"'{your}' is wrong answer ;(. Correct answer was '{correct}'")
        return 5


def question(quest):
    print(f"Question: {quest}")
    return prompt.string("Your answer: ")


def end_string(points, name):
    if points == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}")
