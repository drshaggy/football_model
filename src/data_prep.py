import urllib
import urllib.request as req
import logger
from logger import Levels
import db_manager as db
import pandas as pd

# -------------------------------------------------------------
# This section decides what the function download_all() downloads
# -------------------------------------------------------------
seasons = {'1920',
           '1819',
           '1718',
           '1617',
           '1516',
           '1415',
           '1314',
           '1213',
           '1112',
           }
leagues = {'E0',
           'E1',
           'E2',
           'E3',
           'EC',
           }


# -------------------------------------------------------------
# Downloads all data from www.football-data.co.uk as specified
# above into an sql database.
# -------------------------------------------------------------
def download_all():
    for season in seasons:
        for league in leagues:
            url = 'https://www.football-data.co.uk/mmz4281/' + season + '/' + league + '.csv'
            destination = '../data/' + season + '_' + league + '.csv'
            try:
                req.urlretrieve(url, destination)
                entry = 'Downloaded {}'.format(url)
                csv_to_db(destination, '"{}_{}"'.format(season, league))
                logger.log(entry)
            except urllib.error.HTTPError:
                entry = 'Could not download season {} league {} from {}'.format(season, league, url)
                logger.log(entry, Levels.ERROR)


# -------------------------------------------------------------
# Reads data from csv and imports into sql table. Overwrites
# table every time.
# -------------------------------------------------------------
def csv_to_db(csv_file_path, table_name):
    db.conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
    try:
        read_csv = pd.read_csv(csv_file_path)
        read_csv.to_sql(table_name, db.conn, if_exists='append', index=False)

    except UnicodeDecodeError:
        logger.log('Could not read {} into database table {}'.format(csv_file_path, table_name), Levels.WARNING. )



