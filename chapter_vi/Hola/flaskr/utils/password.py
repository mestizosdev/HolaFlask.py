# -*- coding: utf-8 -*-
import bcrypt


def encrypt(password):
    bytes = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)


def validate(password):
    special_symbols = ['$', '@', '#', '%']

    if len(password) < 9:
        return False, 'Length should be mayor to 9'

    if len(password) > 18:
        return False, 'Length should be not be mayor than 18'

    if not any(char.isdigit() for char in password):
        return False, 'Password should have at least one numeral'

    if not any(char.isupper() for char in password):
        return False, 'Password should have at least one uppercase letter'

    if not any(char.islower() for char in password):
        return False, 'Password should have at least one lowercase letter'

    if not any(char in special_symbols for char in password):
        char = ''.join(map(str, special_symbols))
        return False, f'Password should have at least one of the symbols {char}'

    return True, ''
