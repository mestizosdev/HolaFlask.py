# -*- coding: utf-8 -*-
import bcrypt


def encrypt(password):
    bytes = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
