import sqlite3
import json
from encdec import decrypt
from master_secrets import master_password

conn = sqlite3.connect("pmanager.db")
cur = conn.cursor()
table_name = 'password_details'

# created table
if cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'") is None:
    cur.execute(f'CREATE TABLE {table_name}(url, username, email, password_dict)')

def insert_values(query):
    if cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"):
        cur.execute(query)
        conn.commit()

def update_values(query):
    if cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"):
        cur.execute(query)
        conn.commit()

def show_records(query):
    if cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"):
        for i in cur.execute(query).fetchall():
            for j in i[:-1]: print(j,end=' | ')
            print(decrypt(json.loads(i[-1]), master_password).decode())
        conn.commit()