#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.cli import welkome_user


def main():
    name = welkome_user()
    gcd(name)


if __name__ == "__main__":
    main()
