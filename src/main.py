#!/usr/bin/env python3
import sys
from data_downloader import Downloader
from logger import *
from db_manager import DbManager
from commands import Commands


class Main:
    def __init__(self):
        self.logger = Logger('../logs/')
        self.downloader = Downloader()
        self.db = DbManager('database.db')
        self.parse_args()

    def parse_args(self):
        args = sys.argv
        try:
            if args[1] == Commands.update.name:
                self.downloader.download()
            else:
                self.logger.log("Unknown Command", Levels.ERROR)
        except IndexError:
            self.logger.log("No command supplied", Levels.ERROR)


if __name__ == "__main__":
    app = Main()


