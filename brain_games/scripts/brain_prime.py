#!/usr/bin/env python3

from brain_games.games.prime import play_prime
from brain_games.engine import play_game, welcome_user


def main():
    name = welcome_user()
    name_game = 'prime'
    play_game(name, name_game, play_prime)


if __name__ == '__main__':
    main()
