import sys

from settings import LOGIN, PASSWORD


def start():
    print(f'Hello, {sys.argv[-2]}')


template = sys.argv


def check_user():
    if template[-2] == LOGIN:
        if template[-1] == PASSWORD:
            start()
