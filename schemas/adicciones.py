from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CreateAdicion(BaseModel):
    nombre : str     = Field(..., max_length=50)
    precio : Decimal = Field(..., description="Precio de la adición")
    activo : bool    = True

class ResponseAdicion(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_adiccion : int
    nombre      : str
    precio      : Decimal
    activo      : bool
    creado_en   : Optional[datetime]

class UpdateAdicion(BaseModel):
    nombre : Optional[str]     = None
    precio : Optional[Decimal] = None
    activo : Optional[bool]    = None