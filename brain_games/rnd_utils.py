import random
from brain_games.constant import MATH_OPER


def get_rnd_math_expression() -> str:
    num1, num2 = get_rnd_num(amount=2)
    math_sign = random.choice(MATH_OPER)
    return f'{str(num1)} {math_sign} {str(num2)}'


def get_rnd_choice(lst) -> str:
    return random.choice(lst)


def get_rnd_num(start_num=1, end_num=100, amount=1) -> int:
    match amount:
        case 1:
            return random.randint(start_num, end_num)
        case _:
            return [random.randint(start_num, end_num) for _ in range(amount)]
