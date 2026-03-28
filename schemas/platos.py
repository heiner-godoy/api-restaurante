from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CreatePlato(BaseModel):
    nombre      : str            = Field(..., max_length=100)
    descripcion : Optional[str]  = None
    precio      : Decimal        = Field(..., description="Precio del plato")
    categoria   : str            = Field(..., max_length=50)
    activo      : bool           = True

class ResponsePlato(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_plato    : int
    nombre      : str
    descripcion : Optional[str]
    precio      : Decimal
    categoria   : str
    activo      : bool
    creado_en   : Optional[datetime]

class UpdatePlato(BaseModel):
    nombre      : Optional[str]     = None
    descripcion : Optional[str]     = None
    precio      : Optional[Decimal] = None
    categoria   : Optional[str]     = None
    activo      : Optional[bool]    = None