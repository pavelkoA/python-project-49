#!/usr/bin/env python3
from brain_games.games.even import even
from brain_games.cli import welkome_user
from brain_games.games.engine import game


def main():
    name = welkome_user()
    name_game = 'even'
    game(name, name_game, even)


if __name__ == "__main__":
    main()
