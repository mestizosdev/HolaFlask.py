from sqlalchemy import text
from flaskr.config.database import db
from flask import current_app


def get_version():
    try:
        sql = text('select versions() as version_database')
        with db.engine.connect() as connection:
            result = connection.execute(sql)
            for row in result:
                return row.version_database
    except Exception as e:
        current_app.logger.error(f'Error to get version database {e}')
        return ''
