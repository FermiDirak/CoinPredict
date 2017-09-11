"""Sets up and connects to the Postgres database for data storage"""

import psycopg2
from data_management import config

class Database(object):
    """Interact with the database for CoinPredict"""

    TABLE_NAMES = {
        'historic_raw_data': 'historic_raw_data'
    }

    HISTORIC_SCHEMA = 'time bigint PRIMARY KEY, \
        low money, high money, open money, close money, volume double precision'

    def __init__(self):
        self.conf = config.Config()
        self.connect()

        self.initialize_db()

    def connect(self):
        """creates a connection and a cursor to the PostgreSQL database server"""

        try:
            db_settings = self.conf.read_db_config()

            self.conn = psycopg2.connect(**db_settings)
            self.cur = self.conn.cursor()

        except (psycopg2.DatabaseError) as error:
            print error

    def initialize_db(self):
        """initializes db"""
        self.create_historic_raw_data()


    def create_historic_raw_data(self):
        """creates historic raw data table if it's empty"""

        self.cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables " \
            "WHERE table_name='" + self.TABLE_NAMES['historic_raw_data'] + "');")
        is_historic_table_initalized = self.cur.fetchone()[0]

        print is_historic_table_initalized

        if not is_historic_table_initalized:
            self.cur.execute("CREATE TABLE " + self.TABLE_NAMES['historic_raw_data'] + \
                " (" + self.HISTORIC_SCHEMA + ");")

            self.conn.commit()

            # self.cur.execute("INSERT INTO " + self.TABLE_NAMES['historic_raw_data'] + \
            #     "(time, low, high, open, close, volume) VALUES (0, 0, 0, 0, 0, 0)")


    def close_connection(self):
        """closes db connection"""
        self.conn.close()
