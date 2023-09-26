import prompt
from brain_games.games.lexicon import lexicon


def game(name: str, game_name: str, game_function):
    points = 0
    print(lexicon[game_name])
    while points != 3:
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
    if points == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
