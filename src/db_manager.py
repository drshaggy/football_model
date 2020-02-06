import sqlite3 as sql
import logger
from logger import Levels


conn = None


def connect(name):
    global conn
    path = '../db/' + name
    try:
        conn = sql.connect(path)
        message = "Connected to database '" + name + "'"
        logger.log(message)
    except sql.Error:
        logger.log("Failed to Connect to database", Levels.ERROR)


def disconnect():
    global conn
    logger.log('Database Disconnecting')
    conn.close()

