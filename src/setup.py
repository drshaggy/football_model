import logger
import db_manager as db
from os import path, system
from constants import *


# -------------------------------------------------------------
# Creates necessary directories needed for the program to run
# -------------------------------------------------------------
def first_time_setup():
    is_db_new = False
    for d in DIRS:
        if not path.exists(DIRS[d]):
            message = 'Creating new folder ' + DIRS[d]
            logger.log(message)
            if d == 'DB_DIR':
                is_db_new = True
            system('mkdir ' + DIRS[d])
    if is_db_new:
        db.connect('database.db')
        db.conn.execute('CREATE TABLE SETTINGS (name, value)')
        db.disconnect()
        logger.log("New database created")


# -------------------------------------------------------------
# Execute
# -------------------------------------------------------------
if __name__ == "__main__":
    first_time_setup()