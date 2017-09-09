"""Walks user through setting up and saving a config"""

import ConfigParser

class Config(object):
    """Writes and Reads config files"""

    CONFIG_FILES = {
        'data_extract': 'dataextract_config',
        'svm': 'svm_config',
        'genetic_alg': 'genetic_alg_config'
    }


    def __init__(self):
        pass

    def write_config(self, filename, settings):
        """writes a config to config/$filename.ini with setting vals in settings dict"""

        config = ConfigParser.ConfigParser()
        cfgfile = open('config/' + filename + '.ini', 'w')

        for setting_key, setting_val in settings.items():
            config.set(setting_key, setting_val, True)

        config.write(cfgfile)
        cfgfile.close()

    def read_config(self, filename):
        """reads config file and outputs an object containing settings values"""
        settings = {}

        parser = ConfigParser.SafeConfigParser()
        parser.read('config/' + filename + '.ini')

        for setting_key, setting_val in parser.items(''):
            settings[setting_key] = setting_val

        return settings
