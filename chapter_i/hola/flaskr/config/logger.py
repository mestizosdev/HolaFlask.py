import os
import sys
import logging


def define_logger():
    # Create logs folder if not exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    # Logger
    print(os.path.realpath('.'))
    filename = os.path.join(os.path.realpath('.'), 'logs', 'server.log')
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(asctime)s %(message)s',
        handlers=[logging.FileHandler(filename), logging.StreamHandler(sys.stdout)],
    )
    from flaskr import app

    app.logger.info('Start Flask Server')
