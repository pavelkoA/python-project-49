import prompt


def welkome_user():
    print("Welkome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
