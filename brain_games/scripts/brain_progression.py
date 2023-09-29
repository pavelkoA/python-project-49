#!/usr/bin/env python3

from brain_games.games.progression import play_progression
from brain_games.engine import play_game
from brain_games.cli import welkome_user


def main():
    name = welkome_user()
    name_game = 'progression'
    play_game(name, name_game, play_progression)


if __name__ == '__main__':
    main()
