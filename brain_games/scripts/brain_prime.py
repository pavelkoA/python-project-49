#!/usr/bin/env python3
from brain_games.games.prime import prime
from brain_games.cli import welkome_user


def main():
    name = welkome_user()
    prime(name)


if __name__ == '__main__':
    main()
