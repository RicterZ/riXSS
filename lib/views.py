from lib.settings import *
from lib.models import *
from lib.language.en import *
from lib.authentication import authentication
from lib.valid import RegValidChecker


class BaseHandler(object):

    def render(self, title, template, **kwargs):
        return env.get_template(template).render(title=title, **kwargs)


class IndexHandler(BaseHandler):
    def GET(self):
        return 'Hello world'


class UserHandler(BaseHandler):
    def GET(self, user_id):
        @authentication
        def func():
            return self.render(title=personal_center, template="user.html")
        return func()

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
        return self.render(title=register_, template="reg.html")

    def POST(self):
        input_data = web.input(email='', password='', en_password='')
        valid = RegValidChecker(input_data)
        if valid.is_valid:
            status, message = add_user(input_data.email, input_data.password)
            if not status:
                return self.render(title=register_, template="reg.html", message=message)
            else:
                return web.seeother('/login')
        else:
            return self.render(title=register_, template="reg.html", message=valid.error)


class LoginHandler(BaseHandler):
    def GET(self):
        return self.render(title=sign_in, template="login.html")

    def POST(self):
        input_data = web.input(email='', password='')
        status, message = check_login(input_data.email, input_data.password)
        if not status:
            return self.render(title=sign_in, template="login.html", message=message)
        else:
            web.setcookie("user_id", message)
            web.setcookie("token", get_token(message))
            return web.seeother('/user/%s' % message)


class LogoutHandler(BaseHandler):
    def GET(self):
        pass


