"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    def __repr__(self):
        """Human-readable printout for debugging."""
        cache = {}
        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def __init__(self, name, flavor, price, qty): 
      self.name = name 
      self.flavor = flavor 
      self.price = price 
      self.qty = 0

      self.cache[name] = self 

    def add_stock(self, amount):
       self.qty = self.qty + amount 

    def sell(self, amount): 

      if self.qty == 0: 
        print('Sorry, these cupcakes are sold out')
        return 

      if self.qty < amount: 
        self.qty = 0
        return 

      self.qty -= amount 

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
