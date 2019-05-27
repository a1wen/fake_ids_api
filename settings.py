from logging import config, getLogger
from optparse import OptionParser
from os import environ, path

from tornado_utils2.conf import Config
from tornado_utils2.template_loader import TemplateLoader

from utils.data_file import DataFile

BASE_DIR = path.abspath(path.dirname(__file__))


def get_parser() -> OptionParser:
    """Обработка аргументов командной строки"""
    parser = OptionParser()
    parser.description = 'Megafon Mock'

    # noinspection PyUnusedLocal
    def docker_input_file(*args, **kwargs):
        Config.configure_base64(input())

    parser.add_option(
        '--with-docker-file',
        action='callback',
        callback=docker_input_file,
    )
    return parser


get_parser().parse_args()

if not Config.configured:
    Config.configure(path.join(BASE_DIR, 'config.json'))


SERVER_PORT = environ.get('server_port')
if SERVER_PORT is None:
    SERVER_PORT = Config.get_value('server', 'port')

DEBUG = Config.get_value('server', 'debug')

# Настраиваем логгирование
logging_params = Config.get_value('logging')
config.dictConfig(logging_params)
logger = getLogger('default')

template_loader = TemplateLoader(path.join(BASE_DIR, 'templates'))

with open('./data/good_client_person.csv') as f:
    GOOD_CLIENT_STORAGE = DataFile(f)

with open('./data/bad_client_person.csv') as f:
    BAD_CLIENT_STORAGE = DataFile(f)
