from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime, date
from decimal import Decimal
from models.balance import TipoPeriodo

class CreateBalance(BaseModel):
    tipo_periodo    : TipoPeriodo = Field(..., description="diario | mensual | anual")
    fecha           : date        = Field(..., description="Fecha del balance")
    total_ventas    : Decimal     = Field(default=0)
    total_adiciones : Decimal     = Field(default=0)
    total_gastos    : Decimal     = Field(default=0)
    total_pagos     : Decimal     = Field(default=0)
    utilidad        : Decimal     = Field(default=0)

class ResponseBalance(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_balance      : int
    tipo_periodo    : TipoPeriodo
    fecha           : date
    total_ventas    : Decimal
    total_adiciones : Decimal
    total_gastos    : Decimal
    total_pagos     : Decimal
    utilidad        : Decimal
    creado_en       : Optional[datetime]

class UpdateBalance(BaseModel):
    total_ventas    : Optional[Decimal] = None
    total_adiciones : Optional[Decimal] = None
    total_gastos    : Optional[Decimal] = None
    total_pagos     : Optional[Decimal] = None
    utilidad        : Optional[Decimal] = None