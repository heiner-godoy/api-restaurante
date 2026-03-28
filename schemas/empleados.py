from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from models.empleados import CargoEmpleado

class CreateEmpleado(BaseModel):
    nombre : str = Field(..., min_length=3, max_length=50)
    cargo  : CargoEmpleado = Field(..., description="mesero | cocinero | cajero")
    activo : bool = True

class ResponseEmpleado(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empleado : int
    nombre      : str
    cargo       : CargoEmpleado
    activo      : bool
    creado_en   : Optional[datetime]

class UpdateEmpleado(BaseModel):
    nombre : Optional[str] = None
    cargo  : Optional[CargoEmpleado] = None
    activo : Optional[bool] = None