import random


def get_rnd_choice(lst) -> str:
    return random.choice(lst)


def get_rnd_num(start_num=1, end_num=100, amount=1) -> int:
    match amount:
        case 1:
            return random.randint(start_num, end_num)
        case _:
            return [random.randint(start_num, end_num) for _ in range(amount)]
