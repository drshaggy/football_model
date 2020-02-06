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
        logger.start_logging(LOG_DIR)
        self.first_time_setup()
        db.connect('database.db')
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
        for d in DIRS:
            if not path.exists(DIRS[d]):
                message = 'Creating new folder ' + DIRS[d]
                logger.log(message)
                system('mkdir ' + DIRS[d])

    def cleanup(self):
        db.disconnect()


if __name__ == "__main__":
    app = Main()


