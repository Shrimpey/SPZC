import sqlite3

DB_NAME = 'masterkeys.db'
TABLE_NAME = 'session_master'


def create_db():
    con = sqlite3.connect(f'./{DB_NAME}')
    cur = con.cursor()
    try:
        cur.execute(f'''CREATE TABLE {TABLE_NAME}
                       (session_id TEXT PRIMARY KEY,
                        master_key TEXT NOT NULL)''')
        con.commit()
    except sqlite3.OperationalError:
        pass
    con.close()


if __name__ == '__main__':
    create_db()
