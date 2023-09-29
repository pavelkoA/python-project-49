from brain_games.engine import get_rnd_num


def play_even():
    number = get_rnd_num()
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
