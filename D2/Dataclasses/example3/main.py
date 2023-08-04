"""
Dataclasses pros and cons
"""

import random 
import string
from dataclasses import dataclass, field, astuple, asdict


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


'''
    id : str = field(default_factory=list)
    - lets say the user tries to modify his id which is possible but we dont want it
    - so here is where we add in the init=False to the field() //exclude arguments from initializer
    - sometimes you want to generate a value from other instance variables.. here you use __post_init__() . We implement search_string for a user
    - Now, say you want to change this publicly available search_string to internal, say, protected or private; here we are making it protected
        - for protected use single underscore _protected
        - for private use double underscore __private
    - Now when we print the person, we wish to exclude some attributes from __repr__, especially here _search_string as it's internal
    so we'll omit it from __repr__ by using repr= False
    - Untill now, we could mutate the data using the instance.attribute = "Change value" and get it changed.. How to avoid the below ?
        - person.name = "Sagar" ---> will work
        - person._search_string = "Yoo im changing this" ---> will work
    - Introducing frozen=True will no longer change the object(immutable) after initializing , freezing the object/INSTANCE. SO the above wont
    be possible anymore...
    - kw_only=True forces you to supply the keywords ... Person(name=.., address=..) is only valid. restricts without keywords.
    - match_arg 
'''
@dataclass(frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_address: "list[str]" = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}" #why is it showing an error here?
        





def main() -> None:
    person = Person("Irfan", address = "Madhapur Hyderabad", active=False)
    # person._search_string = "Yoo im changing this"0
    # person.name = "Sagar"
    print(person)


if __name__ == "__main__":
    main()