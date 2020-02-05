import urllib
import urllib.request as req
from logger import *


class Downloader:
    def __init__(self):
        self.seasons = {'1920',
                        '1819',
                        '1718',
                        '1617',
                        '1516',
                        '1415',
                        '1314',
                        '1213',
                        '1112',
                        }
        self.leagues = {'E0',
                        'E1',
                        'E2',
                        'E3',
                        'EC',
                        }
        self.logger = Logger('../logs/')

    def download(self):
        for season in self.seasons:
            for league in self.leagues:
                url = 'https://www.football-data.co.uk/mmz4281/' + season + '/' +  league + '.csv'
                destination = '../data/' + season + '_' + league + '.csv'
                try:
                    req.urlretrieve(url, destination)
                    entry = 'Downloaded ' + url
                    self.logger.log(entry)
                except urllib.error.HTTPError:
                    entry = 'Could not download season ' + season + ' league ' + league + ' from ' + url
                    self.logger.log(entry, Levels.ERROR)