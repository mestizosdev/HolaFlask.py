from sqlalchemy import text


def get_version():
	try:
		from flaskr import db

		sql = text('select version() as version_database')
		with db.engine.connect() as connection:
			result = connection.execute(sql)
			for row in result:
				return row.version_database
	except Exception as e:
		from flaskr import app

		app.logger.error(f'Error to get version database {e}')
		return ''
