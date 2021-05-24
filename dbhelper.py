import sqlite3


class DBHelper:
    def __init__(self, dbname="pipuka.sqlite"):
        self.dbname = dbname

    def setup(self):
        with sqlite3.connect(self.dbname) as con:
            stmt = "CREATE TABLE IF NOT EXISTS items (description text, user text)"
            con.execute(stmt)
            con.commit()

    def add_item(self, item_text, user):
        with sqlite3.connect(self.dbname) as con:
            stmt = "INSERT INTO items (description, user) VALUES (?, ?)"
            args = (item_text, user, )
            con.execute(stmt, args)
            con.commit()

    def get_items(self):
        with sqlite3.connect(self.dbname) as con:
            stmt = "SELECT description FROM items"
            return [x[0] for x in con.execute(stmt)]

    def filter_items(self, owner):
        with sqlite3.connect(self.dbname) as con:
            stmt = "SELECT description FROM items WHERE user = (?)"
            args = (owner, )
            return [x[0] for x in con.execute(stmt, args)]
