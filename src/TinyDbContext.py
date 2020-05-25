from tinydb import TinyDB

class TinyDbContext(object):
  db_name: str
  table_name: str
  database: TinyDB

  def __init__(self, db_name, table_name):
    self.db_name = db_name
    self.table_name = table_name

  def __enter__(self):
    self.database = TinyDB(self.db_name)
    table = self.database.table(self.table_name)
    return table

  def __exit__(self, type, value, traceback):
    self.database.close()
