#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.cli import welkome_user


def main():
    name = welkome_user()
    progression(name)


if __name__ == '__main__':
    main()
