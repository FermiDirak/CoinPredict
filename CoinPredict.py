"""The main function for this program. Run this to update your config,
update your model, and begin predicting in real time"""

from data_management import config
from data_management import database

if __name__ == '__main__':
    CONF = config.Config()

    print 'would you like to setup db config? \'yes\'/\'no\''
    config_db = raw_input()

    if config_db == 'yes':
        CONF.setup_db_config()

    DB = database.Database()

    DB.initialize_db()

    DB.add_historic_raw_data([1499216640, 234, 236.14, 236.14, 234, 16.94774304])

    DB.close_connection()
