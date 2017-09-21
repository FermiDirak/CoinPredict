"""Sets up and connects to the Postgres database for data storage"""

import psycopg2

import CPConstants
from data_management import config

class Database(object):
    """Interact with the database for CoinPredict"""

    # -------- CONSTANTS -------- #

    BTC_USD = 'BTC-USD'
    ETH_USD = 'ETH-USD'


    TABLE_NAMES = {
        'historic_data_btc' : 'historic_data_btc',
        'historic_data_eth' : 'historic_data_eth',

        'feed_data_btc' : 'feed_data_btc',
        'feed_data_eth' : 'feed_data_eth',

        'agg_data_btc' : 'agg_data_btc',
        'agg_data_eth' : 'agg_data_eth'
    }

    HISTORIC_DATA_LABELS = ['time', 'low', 'high', 'open', 'close', 'volume']
    HISTORIC_SCHEMA = 'time bigint PRIMARY KEY, \
        low money, high money, open money, close money, volume double precision'


    # --------- METHODS --------- #

    def __init__(self):
        self.conf = config.Config()
        self.connect()


    def connect(self):
        """creates a connection and a cursor to the PostgreSQL database server"""

        try:
            db_settings = self.conf.read_db_config()

            self.conn = psycopg2.connect(**db_settings)
            self.cur = self.conn.cursor()

        except (psycopg2.DatabaseError) as error:
            print error

    def build_tables(self):
        """builds CoinPredict data table structures. If table already exists,
            then nothing is done"""

        for product in CPConstants.CURRENCIES.values():
            self.build_historic_raw_data(product)


    def build_historic_raw_data(self, product):
        """creates historic raw data table if it's empty"""

        tablename = ''

        # get product table given product name
        if product == CPConstants.CURRENCIES['BTC_USD']:
            tablename = self.TABLE_NAMES['historic_raw_data_btc']
        elif product == CPConstants.CURRENCIES['ETH_USD']:
            tablename = self.TABLE_NAMES['historic_raw_data_eth']
        else:
            return

        self.cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables " \
            "WHERE table_name='" + self.TABLE_NAMES['historic_raw_data'] + "');")
        is_historic_table_initalized = self.cur.fetchone()[0]

        if not is_historic_table_initalized:
            self.cur.execute("CREATE TABLE " + tablename + " (" + self.HISTORIC_SCHEMA + ");")

            self.conn.commit()

    def add_historic_raw_data(self, data):
        """adds entry to historic raw data table"""

        # Check if data is array of 6 elements
        if hasattr(data, "__len__") and data.__len__() == 6:

            self.cur.execute("INSERT INTO " + self.TABLE_NAMES['historic_raw_data'] + \
                " (" + ','.join(str(d) for d in self.HISTORIC_DATA_LABELS) + \
                ") VALUES (" + ', '.join(str(d) for d in data) + ");")
            self.conn.commit()


    def close_connection(self):
        """closes db connection"""
        self.cur.close()
        self.conn.close()
