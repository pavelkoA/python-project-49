import random


def get_rnd_choice(lst) -> str:
    return random.choice(lst)


def get_rnd_num(start_num=1, end_num=100) -> int:
    return random.randint(start_num, end_num)
