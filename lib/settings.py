__author__ = 'Ricter'
import web
import jinja2 as jj


""" Settings for database """
#the database type, `mysql` or `sqlite`
db_type = 'sqlite'

#there is some settings for mysql
db_host = 'localhost'
db_user = 'root'
db_pass = ''
db_name = 'riXSS'

#there is some settings for sqlite3
db_path = './xss.db3'

""" Settings for Develop """
#if in production environment, please set `web.config.debug = False`
#if you are a developer, please set `web.config.debug = True`
web.config.debug = True
TEMPLATES_PATH = 'templates'


""" Some code """
env = jj.Environment(loader=jj.FileSystemLoader(TEMPLATES_PATH), autoescape=True)
if db_type == 'sqlite':
    db = web.database(dbn=db_type, db=db_path)
elif db_type == 'mysql':
    db = web.database(dbn=db_type, db=db_name, host=db_host, user=db_user, pw=db_pass)
