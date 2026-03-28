from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CreateUsuario(BaseModel):
    id_rol      : int = Field(..., description="ID del rol")
    id_empleado : Optional[int] = Field(None, description="ID del empleado")
    username    : str = Field(..., max_length=20)
    password    : str = Field(..., min_length=6)

class ResponseUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_usuario   : int
    id_rol       : int
    id_empleado  : Optional[int]
    username     : str
    activo       : bool
    creado_en    : Optional[datetime]
    ultimo_login : Optional[datetime]

class UpdateUsuario(BaseModel):
    id_rol   : Optional[int] = None
    username : Optional[str] = None
    password : Optional[str] = None
    activo   : Optional[bool] = None