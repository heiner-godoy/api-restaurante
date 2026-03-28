from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class Rol(BaseModel):
    nombre : int = Field(..., max_length=20, description="Nombre del rol")

class ResponseUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_rol : int
    nombre : str
