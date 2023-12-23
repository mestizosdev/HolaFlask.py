from flaskr import app
from colorama import Fore, init

init()


def test_signup():
    url = '/hola/v1/user/signup'
    response = app.test_client().post(
        url,
        json={
            'username': 'test',
            'email': 'test@test.com',
            'password': '123456789Aa@',
        },
    )
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'Json POST result {data}')
    assert response.status_code == 201
