# -*- coding: utf-8 -*-
from sqlalchemy import text
from flaskr.config.database import db
from flask import current_app as app


def find_version():
    try:
        sql = text('select version() as version_database')
        with db.engine.connect() as connection:
            result = connection.execute(sql)
            for row in result:
                return row.version_database
    except Exception as e:
        app.logger.error(f'Error to find database version {e}')
        return 'Not available'
