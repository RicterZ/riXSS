import json
from lib.settings import *
from lib.models import *
from lib.language.en import *
from lib.authentication import authentication, has_obj_permission
from lib.valid import RegValidChecker, AddModuleValidChecker
from lib.utils import now, format_xss_result
from web.webapi import HTTPError


class BaseHandler(object):
    def render(self, title, template, **kwargs):
        return env.get_template(template).render(title=title, **kwargs)


class IndexHandler(BaseHandler):
    def GET(self):
        return 'Hello world'


class RedirectHandler(BaseHandler):
    def GET(self):
        user_id = web.cookies().get('user_id')
        if not user_id:
            web.seeother('/login')
        else:
            web.seeother('/users/%d' % int(user_id))


class UserHandler(BaseHandler):
    def GET(self, user_id):
        @authentication(uid=user_id)
        def func():
            projects = get_user_projects(user_id)
            projects = [{
                "id": i.id,
                "name": i.name,
                "type": i.type,
                "type_name": get_detail(XSS_CORE, i.type, 'name'),
                "created_date": i.created_date
            } for i in projects]
            return self.render(TYPE=0, title=personal_center, template="user.html",
                               modules=get_all_module(user_id=user_id),
                               projects=projects, user_id=user_id,
                               EMAIL=get_detail(USERS, user_id, 'username'))
        return func()

    def POST(self, user_id):
        @authentication(uid=user_id)
        def func():
            web_input = web.input(name='', type=1)
            if web_input.name and user_id:
                add_project(project_name=web_input.name, project_type=web_input.type, user=user_id)
            return web.seeother('/users')
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
        @authentication()
        @has_obj_permission(obj=PROJECTS, obj_id=project_id)
        def func():
            results = format_xss_result(get_xss_result(project_id=project_id))
            return self.render(title="Project %d" % int(project_id), project_id=project_id,
                               template="detail.html", results=results)
        return func()


class XSSResultCleanHandler(BaseHandler):
    def GET(self, project_id):
        @authentication()
        @has_obj_permission(obj=PROJECTS, obj_id=project_id, url="/user")
        def func():
            clean_xss_result(project_id)
            return web.seeother('/projects/%d/results' % int(project_id))
        return func()


class XSSResultDelHandler(BaseHandler):
    def GET(self, project_id, result_id):
        @authentication()
        @has_obj_permission(obj=PROJECTS, obj_id=project_id, url='/user')
        def func():
            del_a_result(result_id)
            return web.seeother('/projects/%d/results' % int(project_id))
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
            return web.seeother('/users')


class LogoutHandler(BaseHandler):
    def GET(self):
        web.setcookie('user_id', '')
        web.setcookie('token', '')
        return web.seeother('/login')


class ProjectHandler(BaseHandler):
    def GET(self, project_id):
        @authentication()
        @has_obj_permission(obj=PROJECTS, obj_id=project_id)
        def func():
            del_project(project_id)
            return web.seeother('/users')
        return func()

    def PUT(self, project_id):
        @authentication()
        @has_obj_permission(obj=PROJECTS, obj_id=project_id)
        def func():
            web_input = web.input(name='', type='')
            modify_project(project_id, web_input.name, web_input.type)
            return {}
        return func()


class DelModuleHandler(BaseHandler):
    def GET(self, module_id):
        @authentication()
        @has_obj_permission(obj=XSS_CORE, obj_id=module_id, url='/modules')
        def func():
            del_module(module_id)
            return web.seeother('/modules')
        return func()


class ModulesHandler(BaseHandler):
    def GET(self):
        @authentication()
        def func():
            user_id = web.cookies().get('user_id')
            return self.render(TYPE=1, EMAIL=get_detail(USERS, user_id, 'username'),
                               title=personal_center, template="user.html",
                               modules=get_all_module(user_id=user_id))
        return func()

    def POST(self):
        @authentication()
        def func():
            user_id = web.cookies().get('user_id')
            web_input = web.input(name='', script='')
            valid = AddModuleValidChecker(web_input)
            if not user_id or not valid.is_valid:
                return web.seeother('/modules')
            add_module(name=web_input.name, script=web_input.script, owner=user_id)
            return web.seeother('/modules')
        return func()


class ModuleHandler(BaseHandler):
    def GET(self, module_id):
        @authentication()
        @has_obj_permission(XSS_CORE, obj_id=module_id, exception=True)
        def func():
            module = get_module_detail(module_id)
            return json.dumps({
                'name': module.name,
                'script': module.script
            })
        return func()

    def PUT(self, module_id):
        @authentication()
        @has_obj_permission(XSS_CORE, obj_id=module_id)
        def func():
            web_input = web.input(name='', script='')
            valid = AddModuleValidChecker(web_input)
            if not valid.is_valid:
                raise HTTPError(403, data=json.dumps({'error': valid.error}),
                                headers={'Content-type': 'application/json'})
            modify_module(module_id, web_input.name, web_input.script)
            return json.dumps({'message': 'successful'})
        return func()