import sqlite3 as sql
import logger
from logger import Levels


conn = None


# -------------------------------------------------------------
# Connects to database in the db directory of name
# 'name'. Creates new database if non existent.
# Input:
#     name - name of database. no path required.
# -------------------------------------------------------------
def connect(name):
    global conn
    path = '../db/' + name
    try:
        conn = sql.connect(path)
        message = "Connected to database '" + name + "'"
        logger.log(message)
    except sql.Error:
        logger.log("Failed to Connect to database", Levels.ERROR)


# -------------------------------------------------------------
# Disconnects from database
# -------------------------------------------------------------
def disconnect():
    global conn
    logger.log('Database Disconnecting')
    conn.close()



