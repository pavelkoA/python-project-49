#!/usr/bin/env python3
from brain_games.games.calc import calc
from brain_games.cli import welkome_user
from brain_games.games.engine import game


def main():
    name = welkome_user()
    name_game = 'calc'
    game(name, name_game, calc)


if __name__ == '__main__':
    main()
