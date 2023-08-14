''' Pydantic models can be used alongside ABCs '''

import abc
from pydantic import BaseModel

class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int
    
    @abc.abstractmethod
    def my_abstract_method(self):
        pass



