import prompt
from brain_games.lexicon import lexicon


GAME_STEP = 3
MAX_POINTS = 3
WON_POINT = 1


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def play_game(game_name: str, game_function):
    points = 0
    name = welcome_user()
    print(lexicon[game_name])
    for _ in range(GAME_STEP):
        quest, correct_answer = game_function()
        your_answer = prompt.string(f"Question: {quest}\n"
                                    f"Your answer: ")
        if correct_answer == your_answer:
            print('Correct!')
            points += WON_POINT
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            break
    if points == MAX_POINTS:
        print(f"Congratulations, {name}!")
