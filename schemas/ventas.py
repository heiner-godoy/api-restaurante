from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
from models.ventas import Metodo

class CreateVenta(BaseModel):
    id_pedido      : int     = Field(..., description="ID del pedido")
    metodo_pago    : Metodo  = Field(..., description="efectivo | transferencia | tarjeta")
    monto_recibido : Decimal = Field(..., description="Monto que entregó el cliente")
    total          : Decimal = Field(..., description="Total a pagar")

    @property
    def cambio(self) -> Decimal:
        return self.monto_recibido - self.total

class ResponseVenta(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_venta       : int
    id_pedido      : int
    metodo_pago    : Metodo
    monto_recibido : Decimal
    cambio         : Decimal
    total          : Decimal
    fecha          : Optional[datetime]
    creado_en      : Optional[datetime]

class UpdateVenta(BaseModel):
    metodo_pago    : Optional[Metodo]   = None
    monto_recibido : Optional[Decimal]  = None
    total          : Optional[Decimal]  = None