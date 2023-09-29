from brain_games.engine import get_rnd_num


def devide_prime(num):
    correct_answer = 'yes'
    for i in range(2, num):
        if num % i == 0:
            correct_answer = 'no'
            break
    return correct_answer


def play_prime():
    num = get_rnd_num()
    correct_answer = devide_prime(num)
    return str(num), correct_answer
