from enum import Enum


class Levels(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3


class Logger:
    def __init__(self, path):
        self.path = path + 'log.txt'

    def log(self, message, level = Levels.INFO):
        log_entry = level.name + ": " + message
        print(log_entry)
