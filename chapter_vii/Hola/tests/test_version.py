from flaskr import app
from colorama import Fore, init

init()


def test_get_version():
    url = '/hola/v1/version'
    response = app.test_client().get(url)
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'Json GET ALL result {data}')
    assert response.status_code == 200
    assert data['application']['name'] == 'HolaFlask.py'
