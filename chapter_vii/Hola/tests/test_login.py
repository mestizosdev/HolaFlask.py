from flaskr.utils.token import generate_confirmation_token
from colorama import Fore, init

init()


def test_signup(app_with_db):
    url = '/hola/v1/user/signup'

    username = 'test'
    email = 'test@test.com'
    password = '123456789Aa@'

    response = app_with_db.post(
        url,
        json={'username': username, 'email': email, 'password': password},
    )
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'JSON POST result {data}')
    assert response.status_code == 201

    # Confirm account
    token = generate_confirmation_token(email)
    url_confirmation = f'/hola/v1/user/signup/confirm/{token}'
    response_confirmation = app_with_db.get(url_confirmation)
    data_confirmation = response_confirmation.get_json()
    print(Fore.GREEN + f'URL {url_confirmation}')
    print(Fore.YELLOW + f'JSON GET result {data_confirmation}')
    assert response_confirmation.status_code == 200

    signin(app_with_db, username, password)


def signin(app_with_db, username: str, password: str):
    url = '/hola/v1/user/signin'
    response = app_with_db.post(
        url,
        json={
            'username': username,
            'password': password,
        },
    )
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'JSON POST result {data}')
    assert response.status_code == 200
