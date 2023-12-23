from colorama import Fore, init

init()


def test_signup(app_with_db):
    url = '/hola/v1/user/signup'
    response = app_with_db.post(
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
