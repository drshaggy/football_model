#!/usr/bin/env python3

import datetime
from os import sys
from logger import Levels
from constants import *


def read_file(level):
    p = LOG_DIR
    date = datetime.datetime.now().strftime("%d%m%y")
    try:
        path = p + '/log-{}.log'.format(date)
        f = open(path, 'r')
        for line in f:
            arr = line.split(' ')
            val = None
            for l in Levels:
                if arr[1][:-1] == str(l.name):
                    val = l.value
            if val >= level.value:
                print(line[:-1])

        f.close()
    except FileNotFoundError:
        print("Invalid Date")


def parse_command():
    if len(sys.argv) == 1:
        read_file(Levels.INFO)
    elif len(sys.argv) >= 2:
        if sys.argv[1] == 'level':
            if len(sys.argv) == 3:
                if sys.argv[2] == 'info':
                    read_file(Levels.INFO)
                if sys.argv[2] == 'warning':
                    read_file(Levels.WARNING)
                if sys.argv[2] == 'error':
                    read_file(Levels.ERROR)
                if sys.argv[2] == 'critical':
                    read_file(Levels.CRITICAL)
            else:
                print("Missing level")


if __name__ == "__main__":
    parse_command()


