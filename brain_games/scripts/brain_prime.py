#!/usr/bin/env python3
from brain_games.games.prime import prime
from brain_games.cli import welkome_user
from brain_games.games.engine import game


def main():
    name = welkome_user()
    name_game = 'prime'
    game(name, name_game, prime)


if __name__ == '__main__':
    main()
