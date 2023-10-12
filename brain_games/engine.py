import prompt
from brain_games.constant import GAME_STEP


def play_game(description: str, game_function):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {name}!\n"
          f"{description}")
    for _ in range(GAME_STEP):
        quest, correct_answer = game_function()
        your_answer = prompt.string(f"Question: {quest}\n"
                                    f"Your answer: ")
        if correct_answer == your_answer:
            print('Correct!')
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
