from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
from models.gastos import CategoriaGasto

class CreateGasto(BaseModel):
    descripcion : str           = Field(..., description="Descripción del gasto")
    monto       : Decimal       = Field(..., description="Monto del gasto")
    categoria   : CategoriaGasto = Field(..., description="hormiga | fijo | extra | mercado | aseo | cocina")

class ResponseGasto(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_gasto    : int
    descripcion : str
    monto       : Decimal
    categoria   : CategoriaGasto
    fecha       : Optional[datetime]
    creado_en   : Optional[datetime]

class UpdateGasto(BaseModel):
    descripcion : Optional[str]           = None
    monto       : Optional[Decimal]       = None
    categoria   : Optional[CategoriaGasto] = None