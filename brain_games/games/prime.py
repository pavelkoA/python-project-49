from brain_games.rnd_utils import get_rnd_num


def is_prime(num):
    correct_answer = 'yes'
    for i in range(2, num):
        if num % i == 0:
            correct_answer = 'no'
            break
    return correct_answer


def play_prime():
    num = get_rnd_num(start_num=2)
    correct_answer = is_prime(num)
    return str(num), correct_answer
