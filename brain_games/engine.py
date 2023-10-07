import prompt
from brain_games.lexicon import lexicon


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def play_game(game_name: str, game_function):
    max_points = 3
    points = 0
    won_point = 1
    name = welcome_user()
    print(lexicon[game_name])
    for _ in range(3):
        quest, correct_answer = game_function()
        print(f"Question: {quest}")
        your_answer = prompt.string("Your answer: ")
        if correct_answer == your_answer:
            print('Correct!')
            points += won_point
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            break
    if points == max_points:
        print(f"Congratulations, {name}!")
