# -*- coding: utf-8 -*-
import os
import sys
import logging


def define_logger(app):
    # Create logs folder if not exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    # Logger
    filename = os.path.join(os.path.realpath('.'), 'logs', 'server.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(asctime)s %(message)s',
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler(sys.stdout),
        ],
    )

    app.logger.info('Start Flask Server')
