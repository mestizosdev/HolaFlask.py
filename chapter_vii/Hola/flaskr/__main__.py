from flaskr import create_app
from flaskr.config.logger import define_logger

app = create_app()

if __name__ == '__main__':
    print('Main Flask Server')
    define_logger()
    app.run()

