"""Write and Retrieve Configs for data extraction, model creation, etc"""

import ConfigParser

class Config(object):
    """Writes and Reads config files"""

    CONFIG_FILES = {
        'data_extract': 'dataextract_config',
        'postgres': 'postgresql',
        'svm': 'svm_config',
        'genetic_alg': 'genetic_alg_config'
    }

    DB_PARAMS = {
        'host': 'localhost',
        'database': 'CoinPredict',
        'user': 'postgres',
        'password': 'postgres'
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

    def ask_config_settings(self, filename, default_settings):
        """asks the user for config settings, and returns custom settings"""

        print 'now modifying %s', filename
        for key, val in default_settings:
            print 'param: %s [defaults to: %s', key, val
            new_val = raw_input()

            if new_val is not None:
                default_settings[key] = new_val

        print 'settings for %s have been modified', filename

        return default_settings


    def write_db_config(self, settings=None):
        """writes the database configuration"""

        if  isinstance(settings, dict):
            for key in self.DB_PARAMS:
                if settings[key] is not None:
                    self.DB_PARAMS[key] = settings[key]

        self.write_config(self.CONFIG_FILES['postgres'], self.DB_PARAMS)

    def read_db_config(self):
        """reads the database config file"""
        return self.read_config(self.CONFIG_FILES['postgres'])
