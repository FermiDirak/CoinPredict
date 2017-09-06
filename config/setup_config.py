"""Walks user through setting up and saving a config"""

import ConfigParser

CONFIG = ConfigParser.ConfigParser()


def write_config():
    """test writes a config to config folder"""

    cfgtest = open('config/test.ini', 'w')

    CONFIG.add_section('test_section')
    CONFIG.set('test_section', 'test_item', True)

    CONFIG.write(cfgtest)
    cfgtest.close()
