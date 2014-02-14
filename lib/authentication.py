__author__ = 'Ricter'
import web
from lib.models import auth_check, is_owner


def authentication(uid=None):
    def has_permission():
        cookies = web.cookies()
        token, user_id = cookies.get('token'), cookies.get('user_id')
        if uid and not uid == user_id:
            return False
        if not token or not user_id:
            return False
        if not auth_check(user_id, token):
            return False
        return True

    def decorator(func):
        def _decorator():
            if has_permission():
                return func
            else:
                def return_a_error():
                    return web.seeother('/login')
                return return_a_error
        return _decorator()

    return decorator


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
