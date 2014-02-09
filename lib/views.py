import json
from lib.settings import *
from lib.models import *
from lib.language.en import *
from lib.authentication import authentication
from lib.valid import RegValidChecker
from lib.utils import now


class BaseHandler(object):
    def render(self, title, template, **kwargs):
        return env.get_template(template).render(title=title, **kwargs)


class IndexHandler(BaseHandler):
    def GET(self):
        return 'Hello world'


class UserHandler(BaseHandler):
    def GET(self):
        @authentication
        def func():
            user_id = web.cookies().get('user_id')
            if not user_id:
                return web.seeother('/login')
            return self.render(title=personal_center, template="user.html",
                               modules=get_all_module(), projects=get_user_projects(user_id),
                               EMAIL=get_detail(USERS, user_id, 'username'))
        return func()

    def POST(self):
        @authentication
        def func():
            user_id = web.cookies().get('user_id')
            web_input = web.input(name='', type=1)
            if web_input.name and user_id:
                add_project(project_name=web_input.name, project_type=web_input.type, user=user_id)
            return web.seeother('/user')
        return func()


class XSScriptHandler(BaseHandler):
    def GET(self, project_id):
        core = get_project_detail(project_id)
        if not core:
            return ''
        code = get_xss_code(core)
        if not code:
            return ''
        xss_script = jj.Template(code)
        return xss_script.render(now_path="http://%s/xss" % web.ctx.env.get('HTTP_HOST'), id=project_id)


class XSSHandler(BaseHandler):
    def GET(self):
        web_input = web.input()
        try:
            project_id = int(web_input.pop('id'))
        except ValueError:
            return ''
        except KeyError:
            return ''
        raw_data = json.dumps(web_input)
        server_data = json.dumps({
            'User-Agent': web.ctx.env.get('HTTP_USER_AGENT'),
            'Request-IP': web.ctx.env.get('REMOTE_ADDR')
        })
        save_raw_data(
            project_id=project_id,
            raw_data=raw_data,
            server_data=server_data,
            got_time=now()
        )
        return ''


class XSSResultHandler(BaseHandler):
    def GET(self, project_id):
        @authentication
        def func():
            pass
        return func()


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
            return web.seeother('/user')


class LogoutHandler(BaseHandler):
    def GET(self):
        pass


class DelProjectHandler(BaseHandler):
    def GET(self, project_id):
        @authentication
        def func():
            user_id = web.cookies().get('user_id')
            if not user_id or not is_owner(user_id=user_id, obj_id=project_id, obj_type=PROJECTS):
                return web.seeother('/login')
            del_project(project_id)
            return web.seeother('/user')
        return func()


class DelModuleHandler(BaseHandler):
    def GET(self, module_id):
        @authentication
        def func():
            user_id = web.cookies().get('user_id')
            if not user_id or not is_owner(user_id=user_id, obj_id=module_id, obj_type=XSS_CORE):
                return web.seeother('/login')
            pass
        return func()