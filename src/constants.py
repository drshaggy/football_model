import platform

if platform.system() == 'Windows':
    DB_DIR = '..\\db'
    DATA_DIR = '..\\data'
    LOG_DIR = '..\\logs'
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    DB_DIR = '../db'
    DATA_DIR = '../data'
    LOG_DIR = '../logs'

DIRS = {}
DIRS['DB_DIR'] = DB_DIR
DIRS['DATA_DIR'] = DATA_DIR
DIRS['LOG_DIR'] = LOG_DIR
