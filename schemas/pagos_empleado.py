from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CreatePagoEmpleado(BaseModel):
    id_empleado : int     = Field(..., description="ID del empleado")
    monto       : Decimal = Field(..., description="Monto del pago")
    nota        : Optional[str] = None

class ResponsePagoEmpleado(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_pago     : int
    id_empleado : int
    monto       : Decimal
    fecha       : datetime
    nota        : Optional[str] = None
    creado_en   : Optional[datetime] = None

class UpdatePagoEmpleado(BaseModel):
    monto : Optional[Decimal] = None
    nota  : Optional[str] = None