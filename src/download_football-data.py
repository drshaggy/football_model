from data_prep import *
import db_manager as db
import logger
import constants as c

# -------------------------------------------------------------
# Script to download all the football data into database
# -------------------------------------------------------------
if __name__ == "__main__":
    logger.start_logging(c.LOG_DIR)
    db.connect('database.db')
    download_all()
