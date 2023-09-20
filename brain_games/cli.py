import prompt


def welkome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
