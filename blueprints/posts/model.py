from pathlib import Path
import os
import sqlite3 as sq
from blueprints.utilities.date_time import datetime_local

SQL_DB = Path(os.getcwd(), 'sqlite.db')
def connect_db():
    with sq.connect(SQL_DB) as conn:
        return conn


class Post():
    """Class of posts to bulletin board \n
    Fields: id, text (the text of the post), 
    parent_id (if not 0, then it is a reply),
    date_created, date_modified.
    a fields variable contains a list of all fields
    for use in creating sql queries.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.text = kwargs.get('text', None)
        self.parent_id = kwargs.get('parent_id', None)
        self.date_created = kwargs.get('date_created', datetime_local())
        self.date_modified = kwargs.get('date_modified', datetime_local())
        
        self.fields = ['id', 'text', 'parent_id', 'date_created', 'date_modified'
            ]
    def create_table(self):
        sql = """create table 'posts' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'text' TEXT,
        'parent_id' INTEGER,
        'date_created' DATE,
        'date_modified' DATE
        );"""
        conn = connect_db()
        cur = conn.cursor()
        res = cur.execute(sql)
        cur.close()
        conn.close()

    def add_record(self):
        d = self.__dict__
        flds = ""
        param_placeholders = ""
        parameters = []
        first_rec = True
        for fld in self.fields:
            if first_rec:
                flds += fld
                param_placeholders += "?"
                first_rec = False
            else:
                flds += f", {fld}"
                param_placeholders += f", ?"
            parameters.append(d[fld])

        sql = f"""INSERT INTO posts ({flds}) VALUES({param_placeholders});"""
        parameters = tuple(parameters)
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql, parameters)
        conn.commit()

        cur.close()
        conn.close()

