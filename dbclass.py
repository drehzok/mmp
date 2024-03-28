from tinydb import TinyDB, Query

class AccountDB():
    def __init__(self, dbpath):
        self.db = TinyDB(dbpath)

    def add(self, item):
        self.db.insert(item)

    def search(self, query):
        return self.db.search(query)
