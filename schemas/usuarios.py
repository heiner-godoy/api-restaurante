from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class Usuarios(BaseModel):
    id_rol : int = Field(..., description = "UK del rol")
    id_empleado : int = Field(..., description = "UK del Empleado")
    username : str = Field(..., max_length = 20, description = "nombre de usuario")
    password : str = Field(..., min_length = 6, description ="Contraseña del usuario")
    activo: bool = Field(default=True, description="Usuario activo")


class ResponseUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_usuario : int
    id_rol : int 
    id_empleado : int
    username : str 
    password : str 
    activo : bool 
    creado_en : Optional[datetime]
    ultimo_login : Optional[datetime]

class UpdateUser(BaseModel):
    id_rol : Optional[int] = None
    username :  Optional[str] = None
    password :  Optional[str] = None
    activo :  Optional[bool] = None
