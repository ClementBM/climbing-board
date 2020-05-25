from typing import List
from Hold import Hold
from TinyDbContext import TinyDbContext
from tinydb import Query

class BoardService():
  db: str
  problem: str

  def __init__(self, db = 'db.json', table = 'problem'):
    self.db = db
    self.table = table

  def insert(self, boulder_problem_sequence: List[Hold]) -> int:
    with TinyDbContext(self.db, self.table) as table:
      sequence = [hold.name for hold in boulder_problem_sequence]
      problem = {
        "hash": hash("".join(sequence)),
        "sequence": sequence
      }
      return table.insert(problem)
  
  def get_by_hash(self, hash) -> dict:
    with TinyDbContext(self.db, self.table) as table:
      query = Query()
      records = table.search(query.hash == hash)
      if len(records) > 1:
        raise Exception('Duplicated boulder problems')
      if len(records) == 0:
        return dict()
      return records[0]
  
  def get_by_id(self, id) -> dict:
    with TinyDbContext(self.db, self.table) as table:
      return table.get(doc_id=id)
  
  def remove(self, doc_id):
    with TinyDbContext(self.db, self.table) as table:
      table.remove(doc_ids=[doc_id])

  def get_all(self):
    with TinyDbContext(self.db, self.table) as table:
      return table.all()