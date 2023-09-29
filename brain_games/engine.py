import prompt
import random
from brain_games.lexicon import lexicon


def welkome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def get_rnd_choice(lst) -> str:
    return random.choice(lst)


def get_rnd_num(start_num=1, end_num=100, amount=1) -> int:
    match amount:
        case 1:
            return random.randint(start_num, end_num)
        case _:
            return [random.randint(start_num, end_num) for _ in range(amount)]


def play_game(name: str, game_name: str, game_function):
    max_points = 3
    points = 0
    print(lexicon[game_name])
    while points != max_points:
        quest, correct_answer = game_function()
        print(f"Question: {quest}")
        your_answer = prompt.string("Your answer: ")
        if correct_answer == your_answer:
            print('Correct!')
            points += 1
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'")
            break
    if points == max_points:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
