import ConfigParser
import os

directory_path = os.path.dirname(__file__)
config_path = os.path.join(directory_path, 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_path)

APP_ROOT_PATH = directory_path.rsplit('/blog', 1)[0]

USERNAME = config.get('CREDENTIAL', 'username')
PASSWORD = config.get('CREDENTIAL', 'password')
SECRET_KEY = config.get('CREDENTIAL', 'secret_key')

DB_FILE = os.path.join(APP_ROOT_PATH, config.get('DATABASE', 'db_file'))
DB_FILE_SQL = os.path.join(APP_ROOT_PATH, config.get('DATABASE', 'db_file_sql'))

STATIC_IMAGES_PATH = os.path.join(APP_ROOT_PATH, config.get('PATH', 'static_images'))
STATIC_AUDIO_PATH = os.path.join(APP_ROOT_PATH, config.get('PATH', 'static_audio'))

LOGNAME = config.get('LOGGING', 'name')
LOGFILENAME = os.path.join(APP_ROOT_PATH, config.get('LOGGING', 'filename'))
LOGLEVEL = config.get('LOGGING', 'level')
LOGFORMAT = config.get('LOGGING', 'format')

IMG_WIDTH_REQUIR = int(config.get('IMGRESIZER', 'width'))
IMG_HEIGHT_REQUIR = int(config.get('IMGRESIZER', 'height'))
WATERMARK_FILE = os.path.join(APP_ROOT_PATH, config.get('IMGRESIZER', 'watermark_file'))
WATERMARK_OPACITY = float(config.get('IMGRESIZER', 'watermark_opacity'))

DEBUG = config.get('OTHER', 'debug')
