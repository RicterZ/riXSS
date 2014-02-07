import sqlite3
from lib.settings import db_path

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
        owner integer not null,
        create_date char(50) not null
    )
""")


db.execute("""
    create table project_results (
        id integer not null primary key autoincrement,
        project_id integer not null,
        xss_location longtext default null,
        xss_toplocation longtext default null,
        xss_title longtext default null,
        xss_opener longtext default null,
        xss_cookies longtext default null,
        xss_referrer longtext default null
    )
""")


db.execute("""
    create table xss_core (
        id integer not null primary key autoincrement,
        name char(50) not null,
        script longtext,
        type integer not null default 0
    )
""")

#add some data of xss-scripts and test account. todo
