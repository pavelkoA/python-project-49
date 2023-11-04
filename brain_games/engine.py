import prompt
from brain_games.constant import NUMBER_OF_STEPS


def run_game(description, get_game_instruction):
    name_player = prompt.string("Welcome to the Brain Games!\n"
                                "May I have your name? ")
    print(f"Hello, {name_player}!\n"
          f"{description}")
    for _ in range(NUMBER_OF_STEPS):
        question, correct_answer = get_game_instruction()
        user_answer = prompt.string(f"Question: {question}\n"
                                    f"Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"Your answer: '{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name_player}!")
            return
    print(f"Congratulations, {name_player}!")
