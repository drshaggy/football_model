import sqlite3 as sql
from logger import *


class DbManager:
    def __init__(self, name):
        self.logger = Logger('../logs/')
        path = '../db/' + name
        try:
            self.conn = sql.connect(path)
        except sql.Error:
            self.logger.log("Failed to Connect to database", Levels.ERROR)

