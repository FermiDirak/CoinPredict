"""Sets up and connects to the Postgres database for data storage"""

import psycopg2
from data_management import config

class Database(object):
    """Interact with the database for CoinPredict"""

    TABLE_NAMES = {
        'historic_raw_data': 'historic_raw_data'
    }

    HISTORIC_SCHEMA = 'time bigint PRIMARY KEY, low money, high money, open money, close money, volume double'

    def __init__(self):
        self.conf = config.Config()
        self.connect()

        self.initialize_db()

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
        """initializes db"""
        self.create_historic_raw_data()


    def create_historic_raw_data(self):
        """creates historic raw data table if it's empty"""
        self.cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables \
            WHERE table_name='%s';", (self.TABLE_NAMES['historic_raw_data']))
        is_historic_table_initalized = bool(self.cur.rowcount)

        if not is_historic_table_initalized:
            self.cur.execute("CREATE TABLE %s (%s);", \
                (self.TABLE_NAMES['historic_raw_data'], self.HISTORIC_SCHEMA))


    def close_connection(self):
        """closes db connection"""
        self.conn.close()
