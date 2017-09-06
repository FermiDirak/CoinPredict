"The main function for this program. Run this to update your config, update your model, and begin predicting in real time"

import time
import gdax

import config.setup_config as setup_config

class CoinPredict(object):
    """ CoinPredict is used to do random things """
    def __init__( self ):
        pass
        
    def poll_gdax(self):
        public_client = gdax.PublicClient()

if __name__ == '__main__':
    
    # set up config
    setup_config.write_config()
