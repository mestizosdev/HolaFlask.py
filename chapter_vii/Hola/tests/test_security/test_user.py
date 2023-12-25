from colorama import Fore, init

init()


def test_list_users(app_with_db):
    url = '/hola/v1/users'
    response = app_with_db.get(url)
    data = response.get_json()
    print(Fore.GREEN + f'URL {url}')
    print(Fore.YELLOW + f'JSON length GET result {len(data)}')
    assert len(data) > 0
