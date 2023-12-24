from colorama import Fore, init

init()


def test_get_version(app_with_db):
    url = '/hola/v1/version'
    response = app_with_db.get(url)
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'JSON GET ALL result {data}')
    assert response.status_code == 200
    assert data['application']['name'] == 'HolaFlask.py'
