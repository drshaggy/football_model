from enum import Enum
import datetime


class Levels(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3


file = None


def start_logging(p):
    date = datetime.datetime.now().strftime("%d%m%y")
    path = p + 'log-' + date + '.txt'
    global file
    file = open(path, 'a')


def log(message, level=Levels.INFO):
    global file
    time = datetime.datetime.now().strftime("%H:%M:%S")
    log_entry = time + ' ' + level.name + ": " + message
    file.write(log_entry)
    file.write('\n')
    print(log_entry)
