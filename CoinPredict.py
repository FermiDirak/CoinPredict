"The main function for this program. Run this to update your config, update your model, and begin predicting in real time"

import time
import gdax

from data_management import config

if __name__ == '__main__':
    config = config.Config()

    print 'would you like to setup db config? \'yes\'/\'no\''
    config_db = raw_input()

    if config_db == 'yes':
        config.setup_db_config()
