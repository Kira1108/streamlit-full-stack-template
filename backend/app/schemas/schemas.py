from pydantic import BaseModel
from typing import List


class IntegerInput(BaseModel):
    value:int
    
    
class ListInput(BaseModel):
    values:List[int]
    
class IntegerOutput(BaseModel):
    value:int