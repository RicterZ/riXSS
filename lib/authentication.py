__author__ = 'Ricter'
import web
from lib.models import auth_check, is_owner


def authentication(func):
    def has_permission():
        try:
            cookies = web.cookies()
            user_id = cookies.user_id
            token = cookies.token
            if not user_id or not token:
                return False
            if not auth_check(user_id, token):
                return False
            return True
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


def has_obj_permission(obj, obj_id, url="/login"):
    def has_permission(_obj=obj, _obj_id=obj_id):
        user_id = web.cookies().get('user_id')
        if not user_id:
            return False
        if not is_owner(user_id=user_id, obj_id=_obj_id, obj_type=_obj):
            return False
        return True

    def decorator(func):
        def _decorator():
            if has_permission(obj, obj_id):
                return func
            else:
                def return_a_error():
                    return web.seeother(url)
                return return_a_error
        return _decorator()

    return decorator
