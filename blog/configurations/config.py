import ConfigParser
import os

directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)

USERNAME = config.get('CREDENTIAL', 'username')
PASSWORD = config.get('CREDENTIAL', 'password')
SECRET_KEY = config.get('CREDENTIAL','secret_key')
DB_FILENAME = config.get('DATABASE', 'db_filename')
DB_FILE_SQL = config.get('DATABASE', 'db_file_sql')
LOGNAME = config.get('LOGGING', 'name')
LOGFILENAME = config.get('LOGGING', 'filename')
LOGLEVEL = config.get('LOGGING', 'level')
LOGFORMAT = config.get('LOGGING', 'format')
DEBUG = config.get('OTHER', 'debug')
