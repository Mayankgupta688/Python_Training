import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
        return None

def create_table(db_file, table_sql):
    try: 
        conn = create_connection(db_file)
        c = conn.cursor()
        c.execute(table_sql)

        sql = '''INSERT INTO employees (id, name, avatar, createdAt) VALUES (1, "Mayank", "Blank", "Dont Know...")'''

        c.execute(sql)

        conn.close()
    except Error as e:
        print(e)

table_sql = """ CREATE TABLE IF NOT EXISTS employees (
                id integer PRIMARY KEY,
                name text NOT NULL,
                avatar text,
                createdAt text
            ); """

create_table(r"D:\SQLite\database\employeeDetails", table_sql)
