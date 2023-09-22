#!/usr/bin/env python3
from brain_games.games.calc import calc
from brain_games.cli import welkome_user


def main():
    name = welkome_user()
    calc(name)


if __name__ == '__main__':
    main()
