from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class CreateRol(BaseModel):
    nombre : str = Field(..., max_length=20)

class ResponseRol(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_rol : int
    nombre : str

class UpdateRol(BaseModel):
    nombre : Optional[str] = None