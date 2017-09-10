"The main function for this program. Run this to update your config, update your model, and begin predicting in real time"

import time
import gdax

from data_management import config

if __name__ == '__main__':
    config = config.Config()

    settings = config.ask_db_settings()

    print settings
