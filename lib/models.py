from lib.settings import db
from lib.language.en import user_already_exist, user_pass_not_match
from utils import make_password, check_password, clean_input, make_token

#settings for table
USERS = 'users'
PROJECTS = 'projects'
XSS_CORE = 'xss_core'
PROJECT_RESULTS = 'project_results'


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
        user_data = user_data[0]
        encode = user_data.password
        user_id = user_data.id
    except IndexError:
        return False, user_pass_not_match
    if not check_password(encode=encode, raw_password=password):
        return False, user_already_exist
    else:
        return True, user_id


def auth_check(user_id, token):
    data = db.select(USERS, what='token', where='id=%d' % int(user_id))[0]
    return data.token == token


def get_token(user_id):
    token = make_token()
    db.update(USERS, where='id=%d' % int(user_id), token=token)
    return token


def save_raw_data(**kwargs):
    db.insert(PROJECT_RESULTS, **kwargs)
    return


def get_project_detail(project_id):
    data = db.select(PROJECTS, where="id=%d" % int(project_id))
    try:
        data = data[0]
    except IndexError:
        return
    else:
        return data.type


def get_xss_code(core_id):
    data = db.select(XSS_CORE, where="id=%d" % int(core_id))
    try:
        data = data[0]
    except IndexError:
        return
    else:
        return data.script