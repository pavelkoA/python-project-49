import prompt
from brain_games.constant import NUMBER_OF_STEPS


def start_engine_games(description: str, game_function):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {name}!\n"
          f"{description}")
    for _ in range(NUMBER_OF_STEPS):
        ask_questions, correct_answer = game_function()
        your_answer = prompt.string(f"Question: {ask_questions}\n"
                                    f"Your answer: ")
        if correct_answer == your_answer:
            print('Correct!')
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            return
    else:
        print(f"Congratulations, {name}!")
