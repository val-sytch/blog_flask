import ConfigParser
import os

directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)

USERNAME = config.get('CREDENTIAL', 'username')
PASSWORD = config.get('CREDENTIAL', 'password')
SECRET_KEY = config.get('CREDENTIAL','secret_key')
DATABASE = config.get('PATH', 'database')
DEBUG = config.get('OTHER', 'debug')
