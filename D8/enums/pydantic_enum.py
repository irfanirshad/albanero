from enum import Enum, IntEnum
from pydantic import BaseModel, ValidationError

class FruitEnum(str, Enum):
    pear = "pear"
    banana = "banana"

class ToolEnum(IntEnum):
    spanner = 1
    wrench = 2


class CookingModel(BaseModel):
    fruit: FruitEnum = FruitEnum.pear
    tool: ToolEnum = ToolEnum.spanner



print(CookingModel()) # fruit=<FruitEnum.pear: 'pear'> tool=<ToolEnum.spanner: 1>
print(CookingModel().fruit) # FruitEnum.pear
# print(CookingModel().fruit.value)  # pear



model2 = CookingModel(tool=2, fruit='banana')
print(model2) # fruit=<FruitEnum.banana: 'banana'> tool=<ToolEnum.wrench: 2>