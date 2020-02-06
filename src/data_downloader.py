import urllib
import urllib.request as req
import logger
from logger import Levels

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


def download():
    for season in seasons:
        for league in leagues:
            url = 'https://www.football-data.co.uk/mmz4281/' + season + '/' + league + '.csv'
            destination = '../data/' + season + '_' + league + '.csv'
            try:
                req.urlretrieve(url, destination)
                entry = 'Downloaded ' + url
                logger.log(entry)
            except urllib.error.HTTPError:
                entry = 'Could not download season ' + season + ' league ' + league + ' from ' + url
                logger.log(entry, Levels.ERROR)
