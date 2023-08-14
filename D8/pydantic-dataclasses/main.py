''' 
Standard Dataclasses over Pydantic's BaseModel but with same data validation....


If you don't want to use Pydantic's 
BaseModel you can instead get the same data validation on standard dataclasses


Github Closed issue comments on the above line::::

"
    How mutable field defaults are handled. 
    BaseModel does not require default_factory for mutable defaults.
    BaseModel handles extra fields.
"

'''

from datetime import datetime
from pydantic.dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None
    
user = User(id=42, name='John Doe', signup_ts='2032-06-21T12:00')
print(user)

'''Some differences between Pydantic dataclasses and BaseModel include:

    How initialization hooks work
    JSON dumping

'''


## Initialization hooks




## JSON DUMPING
