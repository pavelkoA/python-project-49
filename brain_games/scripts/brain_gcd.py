#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.cli import welkome_user
from brain_games.games.engine import game


def main():
    name = welkome_user()
    name_game = 'gcd'
    game(name, name_game, gcd)


if __name__ == "__main__":
    main()
