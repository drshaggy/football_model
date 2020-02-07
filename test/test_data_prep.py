import unittest
import db_manager as db
import data_prep as dp
import os
import logger
import constants


# -------------------------------------------------------------
# Test case for the data_prep.py module
# -------------------------------------------------------------
class DataPrepTestCase(unittest.TestCase):

    def setUp(self):
        logger.start_logging(constants.LOG_DIR)
        constants.DB_DIR = '../db/test.db'

    def test_csv_to_db(self):
        db.connect(constants.DB_DIR)
        dp.csv_to_db('../data/1112_E0.csv', 'test')

    def test_download_all(self):
        db.connect(constants.DB_DIR)
        dp.download_all()

    def tearDown(self):
        db.disconnect()
        #os.system('rm -f ../db/test.db')
