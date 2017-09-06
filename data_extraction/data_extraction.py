"""Extracts raw data from GDAX"""

import time
from datetime import datetime
import gdax

class DataExtraction(object):
    """Used for extracting data from gdax"""

    BTC_USD = 'BTC-USD'
    ETH_USD = 'ETH-USD'

    def __init__(self):
        self.public_client = gdax.PublicClient()

    def latency(self):
        """calculates the latency between user and gdax servers
            in unix time"""
        current_time = time.time()
        gdax_time = self.public_client.get_time()['epoch']

        return gdax_time - current_time

    def get_product(self, product_id):
        """Get details on a product
            https://docs.gdax.com/?python#products"""

        products = self.public_client.get_products()

        return [d for d in products if d['id'] == product_id]

    def download_all_trade_data(self, product_id):
        """download all trade transactions for a given product
            up to the latest trade"""
        pass

    def time_to_epoch(self, date):
        """converts time in format of 'year-month-dateThour:min:secZ
            into epoch time"""

        pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
        epoch = datetime(1970, 1, 1)
        return (datetime.strptime(date, pattern) - epoch).total_seconds()
