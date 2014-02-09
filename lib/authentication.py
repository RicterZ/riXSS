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
                return web.seeother('/login')
            if not auth_check(user_id, token):
                return web.seeother('/login')
            return True
        except AttributeError:
            return web.seeother('/login')

    def decorator(_func=func):
        if has_permission():
            return _func
        else:
            def return_a_error():
                return web.seeother('/login')
            return return_a_error
    return decorator(func)
