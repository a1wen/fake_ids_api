import sys

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.routing import URLSpec
from tornado.web import Application
from tornado_utils2.handlers.ping import PingPongHandler
from app.handlers import *

from settings import logger


def main():
    logger.info('Create web app')
    app = Application(
        handlers=[
            URLSpec(r'/ping', PingPongHandler),
            URLSpec(r'/api/v2/by_passport_data/', ByPassportData),
            URLSpec(r'/api/v2/by_msisdn/', ByMSISDN),
            URLSpec(r'/api/v2/simple_check/', SimpleCheck),
            URLSpec(r'/api/v2/simple_check/lazy/', SimpleCheckLazy),
            URLSpec(r'/api/v2/full_check/', FullCheck),
            URLSpec(r'/api/v2/full_check/lazy/', FullCheckLazy),
        ],
        debug=True,
    )

    logger.info(f'Start HTTP server, port 8000')
    server = HTTPServer(app)
    server.application = app
    server.bind(8000)
    server.start()

    logger.info('Starting IOLoop')
    IOLoop.current().start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('*' * 30)
        logger.info('Hasta la vista, baby!')
        logger.info('*' * 30)
        sys.exit(0)
