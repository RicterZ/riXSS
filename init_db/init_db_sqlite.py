__author__ = 'Ricter'

import sqlite3
from lib.settings import db_path

db = sqlite3.connect(db_path)

db.execute("""
    create table users (
        id integer not null primary key autoincrement,
        username char(50) not null,
        password char(100) not null,
        token char(50) not null
    )
""")

db.execute("""
    create table projects (
        id integer not null primary key autoincrement,
        name char(50) not null,
        type integer not null
    )
""")

db.execute("""
    create table user_project (
        id integer not null primary key autoincrement,
        user_id integer not null,
        project_id integer not null
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

#todo
#add some data of xss-scripts and test account.
