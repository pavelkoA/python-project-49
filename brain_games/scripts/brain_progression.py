#!/usr/bin/env python3

from brain_games.games.progression import progression
from brain_games.cli import welkome_user
from brain_games.games.engine import game


def main():
    name = welkome_user()
    name_game = 'progression'
    game(name, name_game, progression)


if __name__ == '__main__':
    main()
