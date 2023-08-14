
import dataclasses
from typing import List

from pydantic import RootModel
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str 
    friends: List[int] = dataclasses.field(default_factory=lambda: [0])
    

user = User(id='42')
print(RootModel[User](User(id='42')).model_dump_json(indent=4))

'''
JSON output:

{
  "id": 42,
  "name": "John Doe",
  "friends": [
    0
  ]
}

'''

'''
You also have model_dump() which is the primary 
'''