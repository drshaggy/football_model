#!/usr/bin/env python3
import logger
import db_manager as db
from setup import first_time_setup
from constants import *


# -------------------------------------------------------------
# Main class
# -------------------------------------------------------------
class Main:
    def __init__(self):
        # Start logging daemon
        logger.start_logging(LOG_DIR)
        # checks for correct folder structure and makes it if required.
        # Also make new db if required.
        first_time_setup()
        db.connect('database.db')

    def cleanup(self):
        db.disconnect()


# -------------------------------------------------------------
# run
# -------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
