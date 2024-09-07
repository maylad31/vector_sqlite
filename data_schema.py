from typing import Optional,List,Dict
from pydantic import BaseModel as PydanticBaseModel
from pydantic import ValidationError
import numpy as np

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class IndexData(BaseModel):
    vector:np.ndarray
    id: int
    content:str
    metadata:Dict={}
    
    
    
    
if __name__=="__main__":
    pass
        