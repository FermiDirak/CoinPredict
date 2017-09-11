"""Sets up and connects to the Postgres database for data storage"""

import psycopg2
from data_management import config

class Database(object):
    """Interact with the database for CoinPredict"""

    def __init__(self):
        self.conf = config.Config()
        self.connect()

    def connect(self):
        """creates a connection and a cursor to the PostgreSQL database server"""

        conn = None
        try:
            db_settings = self.conf.read_db_config()

            self.conn = psycopg2.connect(**db_settings)
            self.cur = conn.cursor()

        except (psycopg2.DatabaseError) as error:
            print error

    def initialize_db(self):
        """initializes db by checking if one exists and creating or
            updating schemas if it doesn't"""
        pass

    def create_historic_raw_data(self):
        """creates historic raw data table if it's empty"""
        pass

    def close_connection(self):
        """closes db connection"""
        self.conn.close()
