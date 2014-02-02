from lib.settings import *
from lib.models import *
from lib.language.en import *
from lib.valid import RegValidChecker


class BaseHandler(object):

    def render(self, template, **kwargs):
        return env.get_template(template).render(**kwargs)


class IndexHandler(BaseHandler):
    def GET(self):
        return 'Hello world'


class UserHandler(BaseHandler):
    def GET(self, user_id):
        pass

    def POST(self):
        pass


class XSScriptHandler(BaseHandler):
    def GET(self):
        pass


class XSSHandler(BaseHandler):
    def GET(self):
        pass


class XSSResultHandler(BaseHandler):
    def GET(self):
        pass


class RegHandler(BaseHandler):
    def GET(self):
        pass

    def POST(self):
        input_data = web.input(email='', password='', en_password='')
        valid = RegValidChecker(input_data)
        if valid.is_valid:
            status, message = add_user(input_data.email, input_data.password)
            if not status:
                return message
            else:
                return web.seeother('/login')
        else:
            return valid.error


class LoginHandler(BaseHandler):
    def GET(self):
        pass

    def POST(self):
        input_data = web.input(email='', password='')
        status, message = check_login(input_data.email, input_data.password)
        if not status:
            return message
        else:
            return web.seeother('/user/%s' % message)


class LogoutHandler(BaseHandler):
    def GET(self):
        pass


