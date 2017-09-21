"""
For setting up Coin Predict. Run if it's your first time using the project
"""

from data_management import config
from data_management import database

from data_extraction import data_extraction

if __name__ == '__main__':
    DE = data_extraction.DataExtraction()

    CONF = config.Config()

    print 'would you like to setup db config? \'yes\'/\'no\''
    config_db = raw_input()

    if config_db == 'yes':
        CONF.setup_db_config()

    DB = database.Database()

    DB.initialize_db()

    DE.download_all_trade_data(DB, DE.BTC_USD)

    DB.close_connection()
