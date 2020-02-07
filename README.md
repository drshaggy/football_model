# Football Model

## Install Intructions

1. install pandas `pip install pandas`
1. download repo `git clone https://gitlab.com/drshaggy/football_model.git`
1. change directory `cd football_model/src`
1. set up folder structure`python3 setup.py`
1. download football data into database `python3 download_football-data.py`

This gets the folder structure in place and the data downloaded into an sqlite 
database. The seasons and leagues chosen for download currently reside in sets 
in `data_prep.py`, edit these if you want to add/remove data from the downloads.

