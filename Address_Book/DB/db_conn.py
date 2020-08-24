# Address Book DB
import sqlite3 as sq


class Database:
    
    def __init__(self, db):

        self.conn = sq.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY," \
                         "first text, last text, email text)")
        self.conn.commit()

    def fetch(self):

        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, first, last, email):

        self.cur.execute("INSERT INTO contacts VALUES (NULL, ?, ?, ?)", \
                         (first, last, email))
        self.conn.commit()

    def remove(self, id):

        self.cur.execute("DELETE FROM contacts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, first, last, email):

        self.cur.execute("UPDATE contacts SET first = ?, last = ?, email = ?" \
                         "WHERE id = ?", (first, last, email, id))
        self.conn.commit()

    def __del__(self):

        self.conn.close()
