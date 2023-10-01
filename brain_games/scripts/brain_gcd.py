#!/usr/bin/env python3

from brain_games.games.gcd import play_gcd
from brain_games.engine import play_game, welkome_user


def main():
    name = welkome_user()
    name_game = 'gcd'
    play_game(name, name_game, play_gcd)


if __name__ == "__main__":
    main()
