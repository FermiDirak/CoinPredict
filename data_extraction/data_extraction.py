"""Extracts raw data from GDAX"""

import time
from datetime import datetime
import gdax
import csv

class DataExtraction(object):
    """Used for extracting data from gdax"""

    BTC_USD = 'BTC-USD'
    ETH_USD = 'ETH-USD'

    settings = {
        'start_time': 1498867200, #July 1st 00:00:00. When to first start sampling data
        'granularity': 20, #the minimum amount of time between samples
        'step': 3600, #number of seconds to increment api polling by
        'debug_mode': True #display debug information
    }

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

    def get_historic(self, product_id, start_time, end_time, min_granularity):
        """get a list of historic rates between start and end (epoch)
            at speicified minimum level of granularity"""

        start_date = self.epoch_to_date(start_time)
        end_date = self.epoch_to_date(end_time)

        return self.public_client.get_product_historic_rates(product_id, \
            start=start_date, end=end_date, granularity=min_granularity)

    def download_all_trade_data(self, product_id):
        """download all trade transactions for a given product
            up to the latest trade"""

        trade_data = []

        granularity = self.settings['granularity']
        start_time = self.settings['start_time']
        step = self.settings['step']
        end_time = start_time + step
        stop_time = int(time.time())

        while end_time < stop_time:
            trade_data.extend(self.get_historic(product_id, start_time, end_time, granularity))
            start_time += step
            end_time += step

        return trade_data

    def time_to_epoch(self, date):
        """converts time in format of 'year-month-dateThour:min:secZ'
            into epoch time"""

        pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
        epoch = datetime(1970, 1, 1)
        return (datetime.strptime(date, pattern) - epoch).total_seconds()

    def epoch_to_date(self, epochtime):
        """converts epoch time to format of 'year-month-dateThour:min:secZ'"""

        return datetime.utcfromtimestamp(epochtime).isoformat()
