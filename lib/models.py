from lib.settings import db
from lib.language.en import *
from utils import make_password

#settings for table
USERS = 'users'
PROJECTS = 'projects'
USERS_PROJECTS = '%s_%s' % (USERS, PROJECTS)
XSS_CORE = 'xss_core'


def unique(table, field, value):
    data = db.select(table, where='%s="%s"' % (str(field), str(value)))
    try:
        data = data[0]
    except IndexError:
        return True
    else:
        return False


def add_user(username, password):
    if not unique(USERS, 'username', username):
        return False, user_already_exist
    user_id = db.insert('users', username=username, password=make_password(password))
    return True, user_id