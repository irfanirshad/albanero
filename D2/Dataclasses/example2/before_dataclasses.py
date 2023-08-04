
class ManualComment:
    def __init__(self, id: int, text: str) -> None:
        self.__id : int = id # __ to make it immutable and then add @property
        self.__text : str = text
    
    # properties ..this way people can read but cant write to these properties
    @property
    def id(self) -> int:
        return self.__id    
    
    @property
    def text(self) -> str:
        return self.__text
    
    def __repr__(self):
        return f"{self.__class__.__name__} (id = {self.id}, text = {self.text}"
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id,self.text)  == (other.id, other.text)
        else:
            return NotImplemented
    
    def __ne__(self, other):
        result = self.__eq__(other)
        return NotImplemented if result is NotImplemented else not result

    def __hash__(self) -> int:
        return hash((self.__class__, self.id, self.text))   

    
    # FOR SORTING...
    # write le(lessthan), gt(greaterthan), ge(greaterorequalsto)
    # refactor1: use total_ordering from functools so use it in class
    # but since its slower maybe we'll write it ourself manually...
    
    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id,self.text)  <= (other.id, other.text)
        else:
            return NotImplemented
    
    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id,self.text)  >= (other.id, other.text)
        else:
            return NotImplemented
        
    def gt(self, other):
        if other.__class__ is self.__class__:
            return (self.id,self.text)  > (other.id, other.text)
        else:
            return NotImplemented
        
'''
Is the work over? Kinda..
Oh wait, i forgot to add an author. COmments have authors right?
Now I'll have to add in authors to my __init__ as well as make a new @property
for it and then add to __repr__ and __eq__ and __le__ and so on...


I might have to rewrite the entire class now and it will take more time ..
Also, there's a chance I might miss adding it somewhere and we end up with a broken class..


This is the problem.. 

Enter Dataclasses.


PTO to after_dataclasses.py
'''