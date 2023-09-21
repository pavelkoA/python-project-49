#!/usr/bin/env python3
from brain_games.even import even
from brain_games.cli import welkome_user

def main():
    name = welkome_user()
    even(name)

if __name__ == "__main__":
    main()
