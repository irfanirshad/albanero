from validation import check

class Stars:
    def __init__(self, n_stars: int):
        self._number = n_stars
        self.condition()
    
    def condition(self, s: int = None):
        if s:
            check(1 <= s <= 10, f"{self} : {s}")
        else:
            check(1 <= self._number <= 10, f"{self}")
    
    # Prevent external modification
    # no writer here so you can only read it ....
    @property
    def number(self):
        return self._number
    
    # create readable output
    def __str__(self) -> str:
        return f"Stars({self.number})"
    
    def f1(self, n_stars: int) -> int:
        self.condition(n_stars) # precondition
        self._number = n_stars + 5
        self.condition() # Postcondition
        return self._number
    
    def f2(self, n_stars: int) -> int:
        self.
        
    """....TO be continues.... 
    Moved on to example 2 and example 3"""