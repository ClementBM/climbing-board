class Comparable(object):
  """
  https://regebro.wordpress.com/2010/12/13/python-implementing-rich-comparison-the-correct-way/
  """
  def _compare(self, other, method):
    try:
      if type(other) is type(self):
        return method(self._cmpkey, other._cmpkey)
      return NotImplemented
    except (AttributeError, TypeError):
      return NotImplemented

  def __lt__(self, other):
    return self._compare(other, lambda s,o: s < o)

  def __le__(self, other):
    return self._compare(other, lambda s,o: s <= o)

  def __eq__(self, other):
    return self._compare(other, lambda s,o: s == o)

  def __ge__(self, other):
    return self._compare(other, lambda s,o: s >= o)

  def __gt__(self, other):
    return self._compare(other, lambda s,o: s > o)

  def __ne__(self, other):
    return self._compare(other, lambda s,o: s != o)
  
  def __hash__(self):
    try:
      return hash(self._cmpkey)
    except (AttributeError, TypeError):
      return NotImplemented
