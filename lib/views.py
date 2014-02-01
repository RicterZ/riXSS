from lib.settings import *
from lib.models import *


class BaseHandler(object):

    def render(self, template, **kwargs):
        return env.get_template(template).render(**kwargs)


class IndexHandler(BaseHandler):
    def GET(self):
        return 'Hello world'


class UserHandler(BaseHandler):
    def GET(self):
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


class LoginHandler(BaseHandler):
    def GET(self):
        pass

    def POST(self):
        pass


class LogoutHandler(BaseHandler):
    def GET(self):
        pass


