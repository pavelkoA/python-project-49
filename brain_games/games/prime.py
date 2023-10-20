from brain_games.rnd_utils import get_rnd_num
from brain_games.engine import start_engine_games
from brain_games.constant import DESC_PRIME


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_task_game_prime():
    num = get_rnd_num(start_num=2)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return str(num), correct_answer


def start_game_prime():
    start_engine_games(DESC_PRIME, get_task_game_prime)
