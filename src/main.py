#!/usr/bin/env python3
import sys
import data_downloader as downloader
import logger
from logger import Levels
import db_manager as db
from commands import Commands
from os import path, system
from constants import *


class Main:
    def __init__(self):
        # Start logging daemon
        logger.start_logging(LOG_DIR)
        # checks for correct folder structure and makes it
        # if required. Also make new db if required.
        self.first_time_setup()
        db.connect('database.db')
        # parses command line arguments
        self.parse_args()

    def parse_args(self):
        args = sys.argv
        try:
            if args[1] == Commands.update.name:
                downloader.download()
            else:
                logger.log("Unknown Command", Levels.ERROR)
        except IndexError:
            logger.log("No command supplied", Levels.ERROR)
        self.cleanup()

    def first_time_setup(self):
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

    def cleanup(self):
        db.disconnect()


if __name__ == "__main__":
    app = Main()
