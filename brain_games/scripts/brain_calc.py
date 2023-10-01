#!/usr/bin/env python3

from brain_games.games.calc import play_calc
from brain_games.engine import play_game, welkome_user


def main():
    name = welkome_user()
    name_game = 'calc'
    play_game(name, name_game, play_calc)


if __name__ == '__main__':
    main()
