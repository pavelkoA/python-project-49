#!/usr/bin/env python3

from brain_games.games.even import play_even
from brain_games.engine import play_game, welkome_user


def main():
    name = welkome_user()
    name_game = 'even'
    play_game(name, name_game, play_even)


if __name__ == "__main__":
    main()
