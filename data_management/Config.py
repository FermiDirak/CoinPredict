"""Write and Retrieve Configs for data extraction, model creation, etc"""

import ConfigParser

class Config(object):
    """Writes and Reads config files"""

    CONFIG_FILES = {
        'data_extract': 'dataextract_config',
        'postgres': 'postgre',
        'svm': 'svm_config',
        'genetic_alg': 'genetic_alg_config'
    }

    DB_DEFAULT = {
        'host': 'localhost',
        'database': 'coinpredict',
        'user': 'postgres',
        'password': 'postgres',
        'port': '5432'
    }


    def __init__(self):
        pass

    def write_config(self, filename, settings):
        """writes a config to config/$filename.ini with setting vals in settings dict"""

        config = ConfigParser.ConfigParser()
        cfgfile = open('config/' + filename + '.ini', 'w')

        config.add_section(filename)
        for setting_key, setting_val in settings.items():
            config.set(filename, setting_key, setting_val)

        config.write(cfgfile)
        cfgfile.close()

    def read_config(self, filename):
        """reads config file and outputs an object containing settings values"""
        settings = {}

        parser = ConfigParser.SafeConfigParser()
        parser.read('config/' + filename + '.ini')

        for setting_key, setting_val in parser.items(filename):
            settings[setting_key] = setting_val

        return settings

    def ask_config_settings(self, filename, default_settings):
        """asks the user for config settings, and returns custom settings"""

        print 'now modifying ' + filename + '.ini'

        print type(default_settings)

        for key in default_settings:
            print 'param: \'%s\' [defaults to: %s]'%(key, default_settings[key])
            new_val = raw_input()

            if new_val is not '':
                default_settings[key] = new_val

        print default_settings
        print 'settings for %s.ini have been modified'%(filename) + '.'

        return default_settings


    def setup_db_config(self):
        """sets up db config from scratch with user input"""
        settings = self.ask_db_settings()
        self.write_db_config(settings)

    def ask_db_settings(self):
        """asks the user for db config settings, and returns custom settings"""
        return self.ask_config_settings(self.CONFIG_FILES['postgres'], self.DB_DEFAULT)

    def write_db_config(self, settings=None):
        """writes the database configuration"""

        if isinstance(settings, dict):
            for key in self.DB_DEFAULT:
                if settings[key] is None or settings[key] is '':
                    settings[key] = self.DB_DEFAULT[key]

        self.write_config(self.CONFIG_FILES['postgres'], settings)

    def read_db_config(self):
        """reads the database config file"""
        return self.read_config(self.CONFIG_FILES['postgres'])
