import ConfigParser
import os

directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)

APP_ROOT_PATH = directory_path.rsplit('/blog_flask',1)[0]

USERNAME = config.get('CREDENTIAL', 'username')
PASSWORD = config.get('CREDENTIAL', 'password')
SECRET_KEY = config.get('CREDENTIAL','secret_key')

DB_FILENAME = config.get('DATABASE', 'db_filename')
DB_FILE_SQL = config.get('DATABASE', 'db_file_sql')

STATIC_IMAGES_PATH = os.path.join(APP_ROOT_PATH, config.get('PATH','static_images'))
STATIC_AUDIO_PATH = os.path.join(APP_ROOT_PATH, config.get('PATH','static_audio'))
SQL_QUERIES_PATH = os.path.join(APP_ROOT_PATH, config.get('PATH','sql_queries'))

LOGNAME = config.get('LOGGING', 'name')
LOGFILENAME = config.get('LOGGING', 'filename')
LOGLEVEL = config.get('LOGGING', 'level')
LOGFORMAT = config.get('LOGGING', 'format')

IMG_WIDTH_REQUIR = int(config.get('IMGRESIZER','width'))
IMG_HEIGHT_REQUIR = int(config.get('IMGRESIZER','height'))
WATERMARK_FILE = os.path.join(APP_ROOT_PATH,config.get('IMGRESIZER','watermark_file'))
WATERMARK_OPACITY =float(config.get('IMGRESIZER','watermark_opacity'))

DEBUG = config.get('OTHER', 'debug')
