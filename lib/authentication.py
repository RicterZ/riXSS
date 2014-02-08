__author__ = 'Ricter'
import web
from lib.models import auth_check


def authentication(func):
    def has_permission():
        try:
            cookies = web.cookies()
            user_id = cookies.user_id
            token = cookies.token
            if not user_id or not token:
                return False
            return auth_check(user_id, token)
        except AttributeError:
            return False

    def decorator(_func=func):
        if has_permission():
            return _func
        else:
            def return_a_error():
                return web.seeother('/login')
            return return_a_error
    return decorator(func)
