from lib.settings import db
from lib.language.en import user_already_exist, user_pass_not_match
from utils import make_password, check_password, clean_input

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
    user_id = db.insert(USERS, username=username, password=make_password(password))
    return True, user_id


def check_login(username, password):
    user_data = db.select(USERS, where='username="%s"' % clean_input(username))
    try:
        encode = user_data[0].password
    except IndexError:
        return False, user_pass_not_match
    if not check_password(encode=encode, raw_password=password):
        return False, user_already_exist
    else:
        return True, user_data.id