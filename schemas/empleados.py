from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class Empleados(BaseModel):
    nombre : str = Field(...,min_length=3, max_length=50, description = "nombre del empleado")
    cargo : str = Field(..., max_length=20, description="Cargo del empleado")
    activo : bool = Field(..., default=True, description="Estado del empleado")
    
class ResponseEmpleado(BaseModel):
    id_empleado : str
    cargo : str
    nombre : str
    activo : bool
    creado_en : Optional[datetime]
    
class UpdateEmpleado(BaseModel):
    id_empleado : Optional[str]=None
    cargo : Optional[str]=None
    nombre : Optional[str]=None
    activo : Optional[bool]=None
