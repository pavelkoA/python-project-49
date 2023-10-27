import prompt
from brain_games.constant import NUMBER_OF_STEPS


def run_game_engine(description: str, get_question_and_answer):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {name}!\n"
          f"{description}")
    for _ in range(NUMBER_OF_STEPS):
        question, correct_answer = get_question_and_answer()
        your_answer = prompt.string(f"Question: {question}\n"
                                    f"Your answer: ")
        if str(correct_answer) == str(your_answer):
            print('Correct!')
        else:
            print(f"Your answer: '{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
