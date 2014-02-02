import hashlib
import random
import string


def make_password(raw_password):
    salt = ''.join(random.sample(string.letters+string.digits, 12))
    hash_password = hashlib.md5(raw_password + salt).hexdigest()
    return '%s.%s' % (hash_password, salt)


def check_password(encode, raw_password):
    try:
        hash_password, salt = encode.split('.')
    except ValueError:
        return False
    else:
        return hashlib.md5(raw_password + salt).hexdigest() == hash_password


def clean_input(data):
    return data.replace('"', '').replace("'", '')
