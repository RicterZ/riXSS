import hashlib
import random
import string
import datetime
import json
from web import Storage


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


def make_token():
    return ''.join(random.sample(string.letters+string.digits, 20))


def clean_input(data):
    return data.replace('"', '').replace("'", '')


def now():
    return str(datetime.datetime.now()).split('.')[0]


def format_xss_result(data):
    return [{
        'id': i.id,
        'got_time': i.got_time,
        'server_data': json.loads(i.server_data),
        'raw_data': json.loads(i.raw_data)
    } for i in data]